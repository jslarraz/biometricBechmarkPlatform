# imports
from scipy.signal import butter, filtfilt

# filter def
def filter_san18(x, fs):

    # filter parameters
    fc = 0.5        # cutoff frequency
    N = 3           # order
    btype = 'high'  # band pass

    # digital frequency
    Wn = fc/(fs/2)

    # filt
    b, a = butter(N, Wn, btype)
    y = filtfilt(b, a, x)
    return y