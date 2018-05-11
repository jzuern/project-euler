import scipy.optimize
import math
import numpy as np
import matplotlib.pyplot as plt 
import scipy.integrate as integrate


def circle_function(x):
	return -math.sqrt(1.0-(x-1.0)**2)+1

def linear_function(x,n):
	return x/n

def diff(x,n):
	return - circle_function(x) + linear_function(x,n)

# xs = []
# ys = []
# ys2 = []

# n = 2 


# for x in np.arange(0.0,1.0,0.0001):
# 	y = circle_function(x)
# 	xs.append(x)
# 	ys.append(y)
# 	ys2.append(linear_function(x,n))

# plt.plot(xs,ys)
# plt.plot(xs,ys2)

for n in range(1, 10000):

	x0 = 0.5
	root = scipy.optimize.root(diff, x0, n, method='lm').x[0]

	plt.plot(root,linear_function(root,n), 'x')

	# print root
	l_section_area = (4 - math.pi) / 4
	print l_section_area

	integral1 = integrate.quad(lambda x: linear_function(x,n), 0, root)[0]
	integral2 = integrate.quad(lambda x: circle_function(x), root, 1)[0]

	fraction = (integral1+integral2)/l_section_area
	# print "l section area = ", l_section_area
	# print "linear section area = ", integral1
	# print "curved section area = ", integral2

	print "fraction = ", fraction

	if fraction < 0.001:
		print "found!"
		print " n = ", n
		break

