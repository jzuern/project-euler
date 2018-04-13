d = 1000000

frac = 3.0 / 7.0

closest = 1000.0


for x in range(1,d+1):
	max_y = int(frac*x)

	if max_y == 0:
		continue
	if x % 7 == 0 and max_y % 3 == 0:
		continue


	if abs(float(max_y) / x - frac) < closest:
		closest = abs(float(max_y) / x - frac)
		print "closest now: ", max_y, x
		print " error = ", closest

