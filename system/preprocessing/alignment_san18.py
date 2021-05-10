# imports
from numpy import argmax, zeros

def alignment_san18(cycle):

    cycle_aligned = zeros((1, 200), dtype='d')
    if argmax(cycle) < 60:
        cycle_aligned[0][60-argmax(cycle)+5 : 60+len(cycle)-argmax(cycle)-6] = cycle[5:-6]
    else:
        cycle_aligned[0][0] = None
    return cycle_aligned