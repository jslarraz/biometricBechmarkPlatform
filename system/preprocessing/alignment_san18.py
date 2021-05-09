# imports
from numpy import argmax, zeros

def alignment_san18(cycle):
    if argmax(cycle) < 60:
        cycle_aligned = zeros((1, 200), dtype='d')
        cycle_aligned[0][60-argmax(cycle)+5 : 60+len(cycle)-argmax(cycle)-6] = cycle[5:-6]
        return cycle_aligned
    else:
        return None