
max_number_found = 0
max_p = -1

for p in range(0,1000):

	counter = 0
	for i in range(1,p+1):
		for j in range(i,p+1):

			k = p-i-j

			if i+j+k != p:
				continue
			if k < 1:
				continue
			if i == 0 or j == 0:
				continue

			if i*i + j*j == k*k:
				counter += 1

	print "found " + str(counter) + " triangles for p = " + str(p)
	if counter >= max_number_found:
		max_number_found = counter
		max_p = p 

print max_number_found
print p