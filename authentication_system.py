
# authentication system     
from system.enrollment import enrollment
from system.testing import testing
from numpy import *
class authentication_system():
    
    def __init__(self, trainingData, testData, method, metric):
        self.trainingData = trainingData
        self.testData = testData
        self.method = method
        self.metric = metric
    

    def behaviour(self):

        # Enrollment phase
        templatesDB = enrollment().enrollment(self.trainingData, self.method)
        
        # Testing phase
        legit = []
        intruders = [] 
        for signalData in self.testData:        
            confidences = testing().testing(signalData, templatesDB, self.method, self.metric)
            legit.append(confidences['claimed'])
            intruders.append(confidences['others'])                   
                
        far = []
        frr = []
        eer = 0
        th = arange(0, 5, 0.05)
        for thv in th:
            frr.append(sum(legit > thv)/float(size(legit)) )
            far.append(sum(intruders < thv)/float(size(intruders)) )
            if (far[-1] > frr[-1]) and (eer == 0):
                eer = (far[-1] + frr[-1]) / 2 
                

        return th, far, frr, eer      
    
    
# analysis
from system.acquisition import acquisition
#from authentication_system import authentication_system
class analysis():
    
    def analysis_1(self):
        
        # Generate trainingSet for enrollment
        trainingData = acquisition().from_file('signals', 'prrb', 'd1')
        for data in trainingData:
            data['rawSignal'] = data['rawSignal'][:30*300]
            

        # Generate testSet for classification
        testData = acquisition().from_file('signals', 'prrb', 'd1')    
        for data in testData:
            data['rawSignal'] = data['rawSignal'][30*300+1:60*300]
            
        # Run the system
        system = authentication_system(trainingData, testData, 'mean_cycle', 'euclidean_distance')
        return system.behaviour()
    
    
    
    def analysis_2(self):
        
        # EER matrix declaration
        eer_matrix = zeros((12, 12))
        
        bbdd = acquisition().from_file('signals', 'prrb', 'd1')
        
#        for t_training in arange(5,61,5):
        for t_training in arange(30,31,5):    
            for t_test in arange(5,61,5):
                
                print str(t_training) + ' : ' + str(t_test)
                
                # Generate trainingSet for enrollment
                trainingData = []
                for signal in bbdd:
                    data = {}
                    data['fs'] = signal['fs']
                    data['name'] = signal['name']
                    data['rawSignal'] = signal['rawSignal'][:t_training*300]
                    trainingData.append(data)


                # Generate testSet for classification
                testData = []
                for signal in bbdd:
                    data = {}
                    data['fs'] = signal['fs']
                    data['name'] = signal['name']
                    data['rawSignal'] = signal['rawSignal'][t_training*300+1:(t_training+t_test)*300]
                    testData.append(data)

                # Run the system
                system = authentication_system(trainingData, testData, 'mean_cycle', 'euclidean_distance')
                th, far, frr, eer = system.behaviour()
                
                eer_matrix[t_training/5-1][t_test/5-1] = eer

        return eer_matrix
    
    