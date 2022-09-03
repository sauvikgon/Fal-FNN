from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([[0, 0, 0, -0.6, 0]])
x_max = np.array([[0, 0, 0, 0.6, 10]])

#y_param: t,x1,x2,xc

#set condition in x:
#x_min_lower = 0
#x_min_03 = x_min[(0,3)]


#unsafe symbolic states = loc_9
y_min_x1 = 2
y_max_x1 = 3
y_min_x2 = 2
y_max_x2 = 3
Forall(
	x, Implies(x_min <= x <= x_max, Or(Or(y_min_x1 > N(x)[(0,1)], N(x)[(0,1)] > y_max_x1), Or(y_min_x2 > N(x)[(0,2)], N(x)[(0,2)] > y_max_x2)))
)


