# crazy.py
import math
import matplotlib.pyplot as plt


a = 20
b = 10
c = 10

a = int(math.pow(21, 7))
b = int(math.pow(7, 21))
c = int(math.pow(12, 7))

print a
print b
print c

print '\n'
def S_red(q,a,b,c):
	m = b/a
	a = a%q
	b = b%q
	c = c%q

	S1 = (4*m*a*(a-c) + m*a*b - m*a*(a-1)/2)%q
	S2 = ((m*(m-1)/2)*3*a*(a-c))%q
	S3 = ((b - m*a + 1)*(4*(m+1)*a - (3*m+4)*c) + (b - m*a)*(b - m*a + 1)/2)%q

	return (S1+S2+S3)%q



a = 21**7
b = 7**21
c = 12**7
q = 10**9

print(S_red(q,a,b,c))