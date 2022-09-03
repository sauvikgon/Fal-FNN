from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([[0.2, 0.2, 0.8, 0, 0, 0]])
x_max = np.array([[0.7, 0.7, 0.8, 0, 0, 10]])

#t == 0 & 0.7>=x1>=0.2 & 0.7>=x2>=0.2 & 0.8>=v1>=0.8 & 0>=v2>=0 loc()= loc2"
#y_param: x1,x2,v1,v2,t

#unsafe symbolic states = loc_6
y_min_x1 = 2
y_max_x1 = 3
y_min_x2 = 1
y_max_x2 = 2

Forall(
	x, Implies(x_min <= x <= x_max, Or(Or(y_min_x1 > N(x)[(0,0)], N(x)[(0,0)] > y_max_x1), Or(y_min_x2 > N(x)[(0,1)], N(x)[(0,1)] > y_max_x2)))
)


