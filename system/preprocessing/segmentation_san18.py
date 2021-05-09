# imports
from numpy import *

def segmentation_san18(x):
    x = array(x, dtype='d')

    # Threshold calc
    th = (sort(x)[round(len(x)*0.95)] - sort(x)[round(len(x)*0.05)]) / 2.0;

    # Find inflexion points
    pos = array([], dtype='i')
    d = abs(diff(sign(diff(x))))
    for i in range(len(d)):
        if d[i] > 0:
            pos = append(pos, i+1)

    # Compare distance between inflexion points against the threshold
    pos2 = array([], 'i')
    for i in range(1,len(pos)):
        if (x[pos[i]] - x[pos[i-1]]) > th:
            pos2 = append(pos2, pos[i-1] )

    return pos2

