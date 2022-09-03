from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([0.2 , -0.1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0])
x_max = np.array([0.3 , 0.1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 10])

#loc(osc_w_32th_order_1)==loc3 & p <=0.3 & p>=0.2 & q <=0.1 & q>=-0.1 & z==0 & aax1==0 & aax2==0 & aax3==0 & ax1==0 & abx1==0 & abx2==0 & abx3==0 & x1==0 & bax1==0 & bax2==0 & bax3==0 & bx1==0 & bbx1==0 & bbx2==0 & bbx3==0 & x2==0 & cax1==0 & cax2==0 & cax3==0 & cx1==0 & cbx1==0 & cbx2==0 & cbx3==0 & x3==0 & dax1==0 & dax2==0 & dax3==0 & dx1==0 & dbx1==0 & dbx2==0 & dbx3==0 & t==0"

#1*p<=0 & 1*q+0.714286*p>=0
#y_param:p,	q,	aax1,	aax2,	aax3,	ax1,	abx1,	abx2,	abx3,	x1,	bax1,	bax2,	bax3,	bx1,	bbx1,	bbx2,	bbx3,	x2,	cax1,	cax2,	cax3,	cx1,	cbx1,	cbx2,	cbx3,	x3,	dax1,	dax2,	dax3,	dx1,	dbx1,	dbx2,	dbx3,	z,	t,	time,

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
	x, Implies(x_min <= x <= x_max, Or(N(x)[(0,0)] > y_max_p, Add(N(x)[(0,1)], Multiply(constant, N(x)[(0,0)])) < y_min_q))
)



