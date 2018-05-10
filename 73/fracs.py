def computeHCF(a, b):
	while b: a, b = b, a%b
	return a

d = 12000
counter = 0

for divident in range(1,d//2):
	divisor = divident * 2
	while divisor <= divident * 3:
		if computeHCF(divident,divisor) == 1 and divisor <= d:
			counter += 1
			print str(divident) + "/" + str(divisor)
		divisor += 1
# remove "1/2" and "1/3" from results counter
counter -= 2

print "total", counter



