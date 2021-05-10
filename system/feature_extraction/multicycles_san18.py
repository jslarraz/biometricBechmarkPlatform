# imports
from numpy import *

def multicycles_san18(signalData):

    template = []
    for cycle in signalData['cycles']:
        template.append(cycle[31:130])
    return template