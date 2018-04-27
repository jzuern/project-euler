import math
import numpy as np 
import csv


triangles = []

p_0_xs = []
p_0_ys = []
p_1_xs = []
p_1_ys = []
p_2_xs = []
p_2_ys = []

with open('p102_triangles.txt', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		p_0_xs.append(int(row[0]))
		p_0_ys.append(int(row[1]))
		p_1_xs.append(int(row[2]))
		p_1_ys.append(int(row[3]))
		p_2_xs.append(int(row[4]))
		p_2_ys.append(int(row[5]))


def origin_in_triangle(p_x, p_y, p0_x, p0_y, p1_x, p1_y, p2_x, p2_y):

    print p0_x, p0_y, p1_x, p1_y, p2_x, p2_y

    A = 1.0/2 * (-p1_y * p2_x + p0_y * (-p1_x + p2_x) + p0_x * (p1_y - p2_y) + p1_x * p2_y)

    sign = 0
    if A < 0:
    	sign = -1
    else:
    	sign = 1

    s = (p0_y * p2_x - p0_x * p2_y + (p2_y - p0_y) * p_x + (p0_x - p2_x) * p_y) * sign
    t = (p0_x * p1_y - p0_y * p1_x + (p0_y - p1_y) * p_x + (p1_x - p0_x) * p_y) * sign
    
    return s > 0 and t > 0 and (s + t) < 2 * A * sign;



    # det = 1/2 * (-p1_y * p2_x + p0_y * (-p1_x + p2_x) + p0_x * (p1_y - p2_y) + p1_x * p2_y)
    # sign = 1
    # if det < 0:
    #     sign = -1

    # s = (p0_y * p2_x - p0_x * p2_y) * sign
    # t = (p0_x * p1_y - p0_y * p1_x) * sign

    # print s
    # print t 
    
    # return s > 0 and t > 0 and (s + t) < 2 * det * sign


counter = 0
for i in range(0,1000):
	is_in_triangle = origin_in_triangle(0,0,
						p_0_xs[i],p_0_ys[i],
						p_1_xs[i],p_1_ys[i],
						p_2_xs[i],p_2_ys[i])
	print is_in_triangle
	if is_in_triangle:
		counter += 1

print "triangle counter = ", counter