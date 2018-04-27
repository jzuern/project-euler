import math

def isprime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True


def S(M,N):

	smaller = min(M,N)
	bigger =  max(M,N)

	# n_gleich = bigger-smaller-1
	# if n_gleich < 0:
	# 	n_gleich = 0

	n_gleich = max(bigger-smaller-1, 0)
	n_abwechselnd = 2*(smaller-1)

	sliding = 3*n_abwechselnd + 5*n_gleich

	additional = (smaller-1)+(bigger-1)

	# print "n_gleich = ", n_gleich
	# print "n_abwechselnd = ", n_abwechselnd
	# print "additional = ", additional

	return additional + sliding

def inverse_S(M,N):

	smaller = min(M,N)
	bigger =  max(M,N)

	if smaller == bigger:



	else:

		x = (smaller-1)+(bigger-1) + 3*(smaller-1) + 5*max(bigger-smaller-1, 0)
		x = 4*smaller + bigger - 5 + 5*bigger - 5*smaller -5
		x = -1*smaller + 6*bigger -10

	return x





def is_squared_prime(number):

	root = math.sqrt(number)

	if not root.is_integer():
		return False

	return isprime(root)


# MAIN:


# idea: implement inverse function S(m,n) ?
# --> give result and find out if there are integer m and n possible?


counter = 0
for M in range(2,5000):
	for N in range(2,5000):

		result = S(M,N)

		# if result < 100*100:
		if result < 1000000*1000000:
			if is_squared_prime(result):
				print result, M
				counter += 1


M = 3
N = 4


re = S(M,N)
print "S(",M,",",N,") = ", re

re = inverse_S(M,N)
print "S(",M,",",N,") = ", re

print "counter = ", counter

