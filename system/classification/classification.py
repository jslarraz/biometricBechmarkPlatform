
# classification
from numpy import *
class classification():
    
    
    def manhattan_distance(self, template_1, template_2):
        
        dist = sum(abs(template_1 - template_2))
        return dist
    
    
    def euclidean_distance(self, template_1, template_2):

        dist = sum((template_1 - template_2) ** 2)
        return dist
                   
        
