# imports
from numpy import *

def manhattan_san18(template_1, template_2):

    dist = []
    for cycle_1 in template_1:
        for cycle_2 in template_2:
            dist.append(sum(abs(cycle_1 - cycle_2)))
    return min(dist)