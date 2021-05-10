# import
from numpy import mean, arange
from scipy.interpolate import spline

def normalize_san18(cycle, fs):
    #0.53*fs y 1.6*fs
    if ((len(cycle) > (0.53*fs) and len(cycle) < (1.6*fs)) and (cycle[2] < 0)):
        cycle = cycle - mean(cycle)
        cycle = cycle / max(cycle)
        cycle = spline(range(len(cycle)), cycle, arange(0, len(cycle), len(cycle)/127.0))
    else:
        cycle[0] = None
    return cycle