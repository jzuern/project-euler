
import math 
import csv
import numpy as np

filename = 'p099_base_exp.txt'

bases = []
exponents = []

with open(filename) as csvfile:
	reader = csv.reader(csvfile,delimiter=',')
	for row in reader:
		bases.append(row[0])
		exponents.append(row[1])

e_exponents = []

for (base,exponent) in zip(bases,exponents):
	e_exponents.append(float(exponent) * math.log(float(base)))

e_exponents = np.array(e_exponents)
maxindex = e_exponents.argmax()

# increment maxindex by one as line numbers start from 1 but indices start from 0
print "line number = ", maxindex+1
