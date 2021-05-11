# imports
from numpy import arange, size


class system():

    def __init__(self, preprocessing, feature_extractor, classifier):
        self.preprocessing = preprocessing
        self.feature_extractor = feature_extractor
        self.classifier = classifier

    def enrollment(self, signalsData):

        templatesDB = []
        for signalData in signalsData:

            # Preprocessing
            signalData['cycles'] = self.preprocessing(signalData['rawSignal'], signalData['fs'])

            # Feature extraction
            template = self.feature_extractor(signalData)

            # Storage in the DB
            templatesDB.append({'name': signalData['name'], 'template': template})

        self.templates = templatesDB
        return templatesDB

    def testing(self, signalsData, templatesDB):

        confidences = {'legit': [], 'intruder': []}
        for signalData in signalsData:

            # Preprocessing
            signalData['cycles'] = self.preprocessing(signalData['rawSignal'], signalData['fs'])

            # Feature extraction
            template_1 = self.feature_extractor(signalData)

            # Classification
            for template_2 in templatesDB:
                confidence = self.classifier(template_1, template_2['template'])

                if signalData['name'] == template_2['name']:
                    confidences['legit'].append(confidence)
                else:
                    confidences['intruder'].append(confidence)

        self.confidences = confidences
        return confidences

    def behaviour(self, confidences):

        far = []
        frr = []
        eer = 0
        th = arange(0, 25, 0.05)
        for thv in th:
            frr.append(sum(confidences['legit'] > thv)/float(size(confidences['legit'])) )
            far.append(sum(confidences['intruder'] < thv)/float(size(confidences['intruder'])) )
            if (far[-1] > frr[-1]) and (eer == 0):
                eer = (far[-1] + frr[-1]) / 2 * 100

        return th, far, frr, eer