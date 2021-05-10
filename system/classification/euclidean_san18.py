# imports
from numpy import *

def euclidean_distance(template_1, template_2):

    dist = sum((template_1 - template_2) ** 2)
    return dist
