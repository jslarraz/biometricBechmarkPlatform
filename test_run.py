from system import *


# load data set
dataset = {}
dataset['nonin'] = {}
dataset['nonin']['d1'] = from_file('ddbb', 'nonin', 'd1')
dataset['nonin']['d2'] = from_file('ddbb', 'nonin', 'd2')
dataset['nonin']['d3'] = from_file('ddbb', 'nonin', 'd3')
dataset['berry'] = {}
dataset['berry']['d1'] = from_file('ddbb', 'berry', 'd1')
dataset['berry']['d2'] = from_file('ddbb', 'berry', 'd2')
dataset['berry']['d3'] = from_file('ddbb', 'berry', 'd3')


s = system(preprocessing_san18, mean_cycle_san18, manhattan_san18)
s.enrollment(dataset['nonin']['d1'])
s.testing(dataset['nonin']['d1'], s.templates)
th, far, frr, eer = s.behaviour(s.confidences)
print (eer)