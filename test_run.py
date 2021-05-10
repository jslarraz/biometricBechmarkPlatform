from system import *


# load data set
dataset = {}
dataset['nonin'] = {}
dataset['nonin']['d1'] = acquisition.from_file('ddbb', 'nonin', 'd1')
dataset['nonin']['d2'] = acquisition.from_file('ddbb', 'nonin', 'd2')
dataset['nonin']['d3'] = acquisition.from_file('ddbb', 'nonin', 'd3')


# asdf

for signalData in dataset['nonin']['d1']:
    enrol_x = filter_san18()