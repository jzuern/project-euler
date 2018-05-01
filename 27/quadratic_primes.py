def isprime(n):
    '''check if integer n is a prime'''
    n = int(n)
    # make sure n is a positive integer
    if n < 0:
        return False

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



a_min = -999
a_max = 999
b_min = -1000
b_max = 1000
n_max = 1000

# a_min = -0
# a_max = 100
# b_min = -0
# b_max = 100
# n_max = 1000

a_with_max_n = 0
b_with_max_n = 0
max_n = -1

for a in range(a_min,a_max):
    for b in range(b_min,b_max):
        counter = 0

        for n in range(0,n_max):
            result =  n*n + a*n + b
            # print "n = ", n, " result = ", result
            if isprime(result):
                counter += 1
            else:
                if(counter > 0):
                    print "search ended. counter = ", counter, " a = ", a, "b = ", b, " max_n = ", max_n
                if n > max_n:
                    max_n = n
                    a_with_max_n = a
                    b_with_max_n = b
                break


print "a_with_max_n = ", a_with_max_n
print "b_with_max_n = ", b_with_max_n