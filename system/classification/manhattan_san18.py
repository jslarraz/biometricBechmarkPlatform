# imports
from numpy import *

def manhattan_distance(template_1, template_2):

    dist = sum(abs(template_1 - template_2))
    return dist