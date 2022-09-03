from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([[0, 0, 0, 0, 0, -0.6, -0.5, 0]])
x_max = np.array([[0, 0, 0, 0, 0, 0.6, 0.5, 10]])

"t==0 & xc1>=-0.6 & xc1<=0.6 & xc2>=-0.5 & xc2<=0.5 & x4==0 & x3==0 & x2==0 & x1==0 & loc()==L0000"
#y_param: t,x1,x2,x3,x4,xc1,xc2

#unsafe symbolic states = loc_68
y_min_x1 = 2
y_max_x1 = 3
y_min_x2 = 1
y_max_x2 = 2
y_min_x3 = 1
y_max_x3 = 2
y_min_x4 = 1
y_max_x4 = 2

Forall(
	x, Implies(x_min <= x <= x_max, Or(Or(Or(Or(y_min_x1 > N(x)[(0,1)], N(x)[(0,1)] > y_max_x1), Or(y_min_x2 > N(x)[(0,2)], N(x)[(0,2)] > y_max_x2)), Or(y_min_x3 > N(x)[(0,3)], N(x)[(0,3)] > y_max_x3)), Or(y_min_x4 > N(x)[(0,4)], N(x)[(0,4)] > y_max_x4)))
)


