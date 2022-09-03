from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([[0, 0, 0, 0, -0.6, -0.1, 0]])
x_max = np.array([[0, 0, 0, 0, 0.6, 0.1, 10]])


#y_param: t,x1,x2,x3,xc1,xc2

#unsafe symbolic states = loc_8
y_min_x1 = 0
y_max_x1 = 1
y_min_x2 = 2
y_max_x2 = 3
y_min_x3 = 1
y_max_x3 = 2

Forall(
	x, Implies(x_min <= x <= x_max, Or(Or(Or(y_min_x1 > N(x)[(0,1)], N(x)[(0,1)] > y_max_x1), Or(y_min_x2 > N(x)[(0,2)], N(x)[(0,2)] > y_max_x2)), Or(y_min_x3 > N(x)[(0,3)], N(x)[(0,3)] > y_max_x3)))
)



