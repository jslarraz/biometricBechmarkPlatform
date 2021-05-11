# imports
from numpy import arange, size


class system():

    def __init__(self, preprocessing, feature_extractor, classifier):
        self.preprocessing = preprocessing
        self.feature_extractor = feature_extractor
        self.classifier = classifier

    # Enrollment stage
    def enrollment(self, signalsData):

        self.templatesDB = []
        for signalData in signalsData:

            # Preprocessing
            signalData['cycles'] = self.preprocessing(signalData['rawSignal'], signalData['fs'])

            # Feature extraction
            template = self.feature_extractor(signalData)

            # Storage in the DB
            self.templatesDB.append({'name': signalData['name'], 'template': template})

        return signalsData

    # Testing stage
    def testing(self, signalsData):

        confidences = {'legit': [], 'intruder': []}
        for signalData in signalsData:

            # Preprocessing
            signalData['cycles'] = self.preprocessing(signalData['rawSignal'], signalData['fs'])

            # Feature extraction
            template_1 = self.feature_extractor(signalData)

            # Classification
            for template_2 in self.templatesDB:
                confidence = self.classifier(template_1, template_2['template'])

                if signalData['name'] == template_2['name']:
                    confidences['legit'].append(confidence)
                else:
                    confidences['intruder'].append(confidence)

        # Analyse error
        far = []
        frr = []
        eer = 0
        th = arange(0, max(max(confidences['legit']), max(confidences['intruder'])), 0.05)
        for thv in th:
            frr.append(sum(confidences['legit'] > thv)/float(size(confidences['legit'])) )
            far.append(sum(confidences['intruder'] < thv)/float(size(confidences['intruder'])) )
            if (far[-1] > frr[-1]) and (eer == 0):
                eer = (far[-1] + frr[-1]) / 2 * 100

        return th, far, frr, eer