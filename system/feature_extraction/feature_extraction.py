
# feature extraction
from numpy import *
class feature_extraction():
    
    def mean_cycle(self, signalData):

        template = mean(signalData['cycles'], 0)
        template = template[31:130]
        return template