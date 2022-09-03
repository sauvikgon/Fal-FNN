from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([[1.5, 1, 0, 0]])
x_max = np.array([[2.5, 1, 0, 10]])

#x1<= 2.5 & x1 >= 1.5 & x2==1 & t==0 & u==0 & loc()==off_off"
#y_param: x1,x2,t

#unsafe symbolic states = loc_2

y_max_x1 = 1


Forall(
	x, Implies(x_min <= x <= x_max, N(x)[(0,1)] > y_max_x1)
)


