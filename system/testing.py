        
# enrollment
from system.preprocessing.preprocessing_san18 import preprocessing


class testing():
                      
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
            