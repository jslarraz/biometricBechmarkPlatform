from system import *


# load data set
# dataset = {}
# dataset['nonin'] = {}
# dataset['nonin']['d1'] = from_file('ddbb', 'nonin', 'd1')
# dataset['nonin']['d2'] = from_file('ddbb', 'nonin', 'd2')
# dataset['nonin']['d3'] = from_file('ddbb', 'nonin', 'd3')
dataset = from_file('ddbb', 'prrb', 'd1')



s = system(preprocessing_san18, mean_cycle_san18, manhattan_san18)
s.enrollment(dataset)
# s.testing(dataset)