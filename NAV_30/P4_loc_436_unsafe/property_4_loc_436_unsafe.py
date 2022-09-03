from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([4.0000, 0, 21.0000, 0.2000, -0.5000, 0])
x_max = np.array([5.000, 0, 22.0000, 0.5000, 0.5000, 100])


#y_param: x1, t, x2, v1, v2

#unsafe symbolic states = NAV_U17_loc_436
y_min_x1 = 10
y_max_x1 = 11
y_min_x2 = 17
y_max_x2 = 18

Forall(
	x, Implies(x_min <= x <= x_max, Or(Or(y_min_x1 > N(x)[(0,0)], N(x)[(0,0)] > y_max_x1), Or(y_min_x2 > N(x)[(0,2)], N(x)[(0,2)] > y_max_x2)))
)



