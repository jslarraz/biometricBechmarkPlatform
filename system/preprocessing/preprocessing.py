
# Preprocessing
from numpy import *
from scipy.signal import butter, filtfilt
from scipy.interpolate import spline
class preprocessing():
    
    def __init__(self, fs, fc=0.5, N=3, btype='high'):
        
        Wn = fc/(fs/2)
        self.set_filter(N, Wn, btype)


    def preprocessing(self, signalData):
        
        signalData['filteredSignal'] = self.filtering(signalData['rawSignal'])
        signalData['points'] = self.detection(signalData['filteredSignal'])
        signalData['cycles'] = self.segmentation(signalData['filteredSignal'], signalData['points'])

        return signalData
        
    def set_filter(self, N, Wn, btype):
        
        b, a = butter(N, Wn, btype)
        self.filter = {'b': b, 'a': a}
    
    
    def filtering(self, x):     
        
        y = filtfilt(self.filter['b'], self.filter['a'], x)
        return y    
    
    
    def detection(self, x):
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

    
    def segmentation(self, x, pos):
        
        # Eliminamos las muestras iniciales
        x = x[pos[0]:]
        pos = pos - pos[0]

        # Generamos una matriz de realizaciones
        cycles = zeros((len(pos)-1, 200), dtype='d')
        malas = array([], 'i')
        for i in range(len(pos)-1):
            cycle = x[pos[i]:pos[i+1]-1]

            cycle = self.normalize(cycle)
            if cycle == None:
                malas = append(malas, i)
                continue
            
            cycle = self.alignment(cycle)
            if cycle == None:
                malas = append(malas, i)
                continue

            cycles[i] = cycle

        cycles = delete(cycles, malas, 0)
        return cycles
    
    
    
    def normalize(self, cycle):
        #0.53*fs y 1.6*fs
        if ((len(cycle) > 159 and len(cycle) < 480) and (cycle[2] < 0)):   
            cycle = cycle - mean(cycle)
            cycle = cycle / max(cycle)
            cycle = spline(range(len(cycle)), cycle, arange(0, len(cycle), len(cycle)/127.0))
            return cycle
        else:
            return None
        
    def alignment(self, cycle):
        if argmax(cycle) < 60:
            cycle_aligned = zeros((1, 200), dtype='d')
            cycle_aligned[0][60-argmax(cycle)+5 : 60+len(cycle)-argmax(cycle)-6] = cycle[5:-6]
            return cycle_aligned
        else:
            return None
        