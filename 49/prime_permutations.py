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


def ispermutation(a, b):

	c = [0,0,0,0,0,0,0,0,0,0]

	while (a):
		c[a%10] += 1
		a/=10
	while b:
		c[b%10] -= 1
		b/=10

	res = 1;
	for cs in c:
		res = res and cs==0;

	if res == 1:
		return True
	else:
		return False


for number in range(0,9999):

	number1 = number
	number2 = number+3330
	number3 = number+6660

	if isprime(number1) and isprime(number2) and isprime(number3):
		if ispermutation(number1,number2) and ispermutation(number2,number3):
			print number1,number2,number3
