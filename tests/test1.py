from system import *

s = system(preprocessing_san18, multicycles_san18, manhattan_san18)

s.enrollment(from_file('ddbb', 'nonin', 'd1', 0, 30))
th, far, frr, eer = s.testing(from_file('ddbb', 'nonin', 'd1', 30, 60))
print(eer)

s.enrollment(from_file('ddbb', 'berry', 'd1', 0, 30))
th, far, frr, eer = s.testing(from_file('ddbb', 'berry', 'd1', 30, 60))
print(eer)


s.enrollment(from_file('ddbb', 'nonin', 'd2', 0, 30))
th, far, frr, eer = s.testing(from_file('ddbb', 'nonin', 'd2', 30, 60))
print(eer)

s.enrollment(from_file('ddbb', 'berry', 'd2', 0, 30))
th, far, frr, eer = s.testing(from_file('ddbb', 'berry', 'd2', 30, 60))
print(eer)





# s.enrollment(from_file('ddbb', 'prrb', 'd1', 0, 30))
# th, far, frr, eer = s.testing(from_file('ddbb', 'prrb', 'd1', 30, 60))
# print(eer)