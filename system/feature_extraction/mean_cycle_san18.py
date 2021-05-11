# imports
from numpy import *

def mean_cycle_san18(signalData):

    template = mean(signalData['cycles'], 0)
    template = [template[31:130]]
    return template