from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([12.0 , 9.0 , 6.0 , 0 , -1 , 1 , 0 , 3.0 , 3.0 , 0])
x_max = np.array([12.0 , 9.0 , 6.0 , 100 , 1 , 3 , 0 , 3.0 , 3.0 , 5])

#loc(ACCS03) == crs_crs_crs & x0 == 12.0 & x1 == 9.0 & x2 == 6.0 & autd101 == 3.0 & autd201 == 3.0 & c1 >= 0 & c1 <= 100 & c2 >= -1 & c2 <= 1 & c3 >= 1 & c3 <= 3 & t == 0.0

#loc=8 & 1*autd201 <= 3
#y_param: x0,	x1,	x2,	c1,	c2,	c3,	t,	autd101,	autd201,	time,

#safe symbolic states = 

y_max_p = 3
"""
Forall(
	x, Implies(x_min <= x <= x_max, Or(N(x)[(0,0)] > y_max_p, N(x)[(0,0)] > Minus))
)

"""
Forall(
	x, Implies(x_min <= x <= x_max, Or(N(x)[(0,8)] > y_max_p))
)



