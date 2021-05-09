# imports
from filter_san18 import *
from segmentation_san18 import *
from normalization_san18 import *
from alignment_san18 import *


def preprocessing_san18(x, fs):

    # Filter
    x = filter_san18(x, fs)

    # Segmentation
    pos = segmentation_san18(x)

    # Eliminamos las muestras iniciales
    x = x[pos[0]:]
    pos = pos - pos[0]

    # Generamos una matriz de realizaciones
    cycles = zeros((len(pos)-1, 200), dtype='d')
    malas = array([], 'i')
    for i in range(len(pos)-1):
        cycle = x[pos[i]:pos[i+1]-1]

        cycle = normalize_san18(cycle)
        if cycle == None:
            malas = append(malas, i)
            continue

        cycle = alignment_san18(cycle)
        if cycle == None:
            malas = append(malas, i)
            continue

        cycles[i] = cycle

    cycles = delete(cycles, malas, 0)
    return cycles