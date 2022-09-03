
from dnnv.properties import *
import numpy as np

N = Network("N")

x_min = np.array([12, 24, 0, 0, 0, 0,0,0])
x_max = np.array([13, 25, 0, 0, 0, 0,0,10])

#initially = "t == 0 & x1 <= 13.00 & x1 >= 12.00 & x2 <=25.00 & x2 >= 24.00 & loc(NavigationBenchmark)==loc_612 & 0.00<=v1<=0.00 & 0.00<=v2<=0.00 & v11 == 0 & v22 == 0" 
#1*x1>=11 & 1*x1<=12 & 1*x2>=16 & 1*x2<=17"
#y_param: x1,	x2,	v1,	v2,	t,	v11,	v22,	time,	x1',	x2',	v1',	v2',	t',	v11',	v22'

#unsafe symbolic states = loc_181
y_min_x1 = 3
y_max_x1 = 4
y_min_x2 = 18
y_max_x2 = 19

Forall(
	x, Implies(x_min <= x <= x_max, Or(Or(y_min_x1 > N(x)[(0,0)], N(x)[(0,0)] > y_max_x1), Or(y_min_x2 > N(x)[(0,1)], N(x)[(0,1)] > y_max_x2)))
)









