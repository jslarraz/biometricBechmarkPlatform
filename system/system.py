

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
            template = self.feature_extractor(signalData['cycles'])

            # Storage in the DB
            templatesDB.append({'name': signalData['name'], 'template': template})

        self.templates = templatesDB
        return templatesDB

    def testing(self, signalData, templatesDB):

        # Preprocessing
        signalData['cycles'] = self.preprocessing(signalData['rawSignal'], signalData['fs'])
        print signalData['cycles'].shape

        # Feature extraction
        template_1 = self.feature_extractor(signalData)

        # Classification
        confidences = {'others': []}
        for template_2 in templatesDB:
            confidence = self.classifier(template_1, template_2['template'])

            if signalData['name'] == template_2['name']:
                confidences['claimed'] = confidence
            else:
                confidences['others'].append( confidence )

        return confidences


    # #from numpy import arange, size
    # from scipy import arange, size
    # def behaviour(self):
    #
    #     # Enrollment phase
    #     templatesDB = self.enrollment(self.trainingData)
    #
    #     # Testing phase
    #     legit = []
    #     intruders = []
    #     for signalData in self.testData:
    #         confidences = self.testing(signalData, templatesDB)
    #         legit.append(confidences['claimed'])
    #         intruders.append(confidences['others'])
    #
    #     far = []
    #     frr = []
    #     eer = 0
    #     th = arange(0, 5, 0.05)
    #     for thv in th:
    #         frr.append(sum(legit > thv)/float(size(legit)) )
    #         far.append(sum(intruders < thv)/float(size(intruders)) )
    #         if (far[-1] > frr[-1]) and (eer == 0):
    #             eer = (far[-1] + frr[-1]) / 2
    #
    #
    #     return th, far, frr, eer