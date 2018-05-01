import fractions

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount


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



max_ = -1.0
n_max = -1


primes = []
for c in range(3,10000):
	if isprime(c):
		primes.append(c)


i = 0

n = 2
while n < 1000000:

	print n

	phi_n = phi(n)

	quotient = float(n)/phi_n

	max_ = quotient
	n_max = n
	print "new max = ", max_, " with n = ", n_max
	
	n = n*primes[i]
	i += 1


print "final max = ", max_, " with n = ", n_max