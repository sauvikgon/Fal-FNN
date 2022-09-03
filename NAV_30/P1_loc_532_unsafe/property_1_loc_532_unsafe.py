from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([4.0000, 0, 21.0000, 0.2000, -0.5000, 0])
x_max = np.array([5.000, 0, 22.0000, 0.5000, 0.5000, 100])

#t == 0 & x1<=5.0000 & x1>=4.0000 & x2<=22.0000 & x2>=21.0000 & v1<=0.5000 & v1>=0.2000 & v2<=0.5000 & v2>=-0.5000


#y_param: x1, t, x2, v1, v2

#unsafe symbolic states = loc_532
y_min_x1 = 6
y_max_x1 = 7
y_min_x2 = 21
y_max_x2 = 22

Forall(
	x, Implies(x_min <= x <= x_max, Or(Or(y_min_x1 > N(x)[(0,0)], N(x)[(0,0)] > y_max_x1), Or(y_min_x2 > N(x)[(0,2)], N(x)[(0,2)] > y_max_x2)))
)



