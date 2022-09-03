from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([0.2, -0.1, 0, 0])
x_max = np.array([0.3, 0.1, 0, 10])

#loc(oscillator_template_1) == loc3 & t == 0 & p <= 0.3 & p >= 0.2 & q <= 0.1 & q >= -0.1"

#1*p<=0 & 1*q+0.714286*p>=0
#y_param: p,q,t

#unsafe symbolic states = osc_loc_1

y_max_p = 0
y_min_q = 0
constant = 0.714286
"""
Forall(
	x, Implies(x_min <= x <= x_max, Or(N(x)[(0,0)] > y_max_p, N(x)[(0,0)] > Minus))
)

"""
Forall(
	x, Implies(x_min <= x <= x_max, Or(N(x)[(0,0)] > y_max_p, Add(N(x)[(0,0)], Multiply(constant, N(x)[(0,1)])) > y_min_q))
)



