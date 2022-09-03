from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([4.0000, 0, 21.0000, 0.2000, -0.5000, 0])
x_max = np.array([5.000, 0, 22.0000, 0.5000, 0.5000, 100])

#t == 0 & x1<=5.0000 & x1>=4.0000 & x2<=22.0000 & x2>=21.0000 & v1<=0.5000 & v1>=0.2000 & v2<=0.5000 & v2>=-0.5000

#1*x1>=11 & 1*x1<=12 & 1*x2>=16 & 1*x2<=17"
#y_param: x1, t, x2, v1, v2

#unsafe symbolic states = NAV_U17_loc_412
y_min_x1 = 11
y_max_x1 = 12
y_min_x2 = 16
y_max_x2 = 17

Forall(
	x, Implies(x_min <= x <= x_max, Or(Or(y_min_x1 > N(x)[(0,0)], N(x)[(0,0)] > y_max_x1), Or(y_min_x2 > N(x)[(0,2)], N(x)[(0,2)] > y_max_x2)))
)


