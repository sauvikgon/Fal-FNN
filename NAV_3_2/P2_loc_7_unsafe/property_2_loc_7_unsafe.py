from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([[0, 0, 0, -0.6, 0]])
x_max = np.array([[0, 0, 0, 0.6, 10]])


#y_param: t,x1,x2,xc

#unsafe symbolic states =loc_7
y_min_x1 = 2
y_max_x1 = 3
y_min_x2 = 0
y_max_x2 = 1

Forall(
	x, Implies(x_min <= x <= x_max, Or(Or(y_min_x1 > N(x)[(0,1)], N(x)[(0,1)] > y_max_x1), Or(y_min_x2 > N(x)[(0,2)], N(x)[(0,2)] > y_max_x2)))
)



