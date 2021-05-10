

class system():
    def __init__(self, preprocessing, feature_extractor, classifier):
        self.preprocessing = preprocessing
        self.feature_extractor = feature_extractor
        self.classifier = classifier


    def enrollment(self, signalsData):

        preprocessing_chains = {}
        templatesDB = []
        for signalData in signalsData:

            # Create the preprocessing chain
            if not( signalData['fs'] in preprocessing_chains.keys() ):
                preprocessing_chains[signalData['fs']] = preprocessing_san18(signalData['fs'])

            preprocessing_chain = preprocessing_chains[signalData['fs']]

            # Preprocessing
            signalData = preprocessing_chain.preprocessing(signalData)

            # Feature extraction
            template = eval("feature_extraction()." + method + "(signalData)")

            # Storage in the DB
            templatesDB.append({'name': signalData['name'], 'template': template})

        return templatesDB





    def testing(self, signalData, templatesDB, method, metric):


        # Create preprocessing chain
        preprocessing_chain = preprocessing(signalData['fs'])

        # Preprocessing
        signalData = preprocessing_chain.preprocessing(signalData)
        print signalData['cycles'].shape


        # Feature extraction
        template_1 = eval("feature_extraction()." + method + "(signalData)")

        # Classification
        confidences = {'others': []}
        for template_2 in templatesDB:
            confidence = eval("classification()." + metric + "(template_1, template_2['template'])")

            if signalData['name'] == template_2['name']:
                confidences['claimed'] = confidence
            else:
                confidences['others'].append( confidence )

        return confidences



    def behaviour(self):

        # Enrollment phase
        templatesDB = enrollment().enrollment(self.trainingData, self.method)

        # Testing phase
        legit = []
        intruders = []
        for signalData in self.testData:
            confidences = testing().testing(signalData, templatesDB, self.method, self.metric)
            legit.append(confidences['claimed'])
            intruders.append(confidences['others'])

        far = []
        frr = []
        eer = 0
        th = arange(0, 5, 0.05)
        for thv in th:
            frr.append(sum(legit > thv)/float(size(legit)) )
            far.append(sum(intruders < thv)/float(size(intruders)) )
            if (far[-1] > frr[-1]) and (eer == 0):
                eer = (far[-1] + frr[-1]) / 2


        return th, far, frr, eer      