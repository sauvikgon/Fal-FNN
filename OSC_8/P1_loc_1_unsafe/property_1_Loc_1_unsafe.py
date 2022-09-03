from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([0.2 , -0.1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0])
x_max = np.array([0.3 , 0.1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 10])

#loc(osc_w_8th_order_1)==loc3 p<=0.3 & p>=0.2 & q<=0.1 & q>=-0.1 & z==0 & ax1==0 & ax2==0 & ax3==0 & x1 == 0 & bx1==0 & bx2==0 & bx3==0 & t==0"

#1*p<=0 & 1*q+0.714286*p>=0
#y_param: p,q,t,ax1,ax2,ax3,x1,bx1,bx2,bx3,z,time

#unsafe symbolic states = OSC_8_loc_1

y_max_p = 0
y_min_q = 0
constant = 0.714286
"""
Forall(
	x, Implies(x_min <= x <= x_max, Or(N(x)[(0,0)] > y_max_p, N(x)[(0,0)] > Minus))
)

"""
Forall(
	x, Implies(x_min <= x <= x_max, Or(N(x)[(0,0)] > y_max_p, Add(N(x)[(0,1)], Multiply(constant, N(x)[(0,0)])) < y_min_q)))



