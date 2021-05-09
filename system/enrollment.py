        
# enrollment
from system.preprocessing.preprocessing import preprocessing


class enrollment():
                      
    def enrollment(self, signalsData, method):
              
        preprocessing_chains = {}
        templatesDB = []
        for signalData in signalsData:
            
            # Create the preprocessing chain 
            if not( signalData['fs'] in preprocessing_chains.keys() ):
                preprocessing_chains[signalData['fs']] = preprocessing(signalData['fs'])  
                
            preprocessing_chain = preprocessing_chains[signalData['fs']]
            
            # Preprocessing
            signalData = preprocessing_chain.preprocessing(signalData)
            
            # Feature extraction
            template = eval("feature_extraction()." + method + "(signalData)")
                            
            # Storage in the DB
            templatesDB.append({'name': signalData['name'], 'template': template})
                   
        return templatesDB               
            