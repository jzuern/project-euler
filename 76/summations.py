summations = 101*[1]

summations[1] = 1
summations[2] = 1
summations[3] = 2
summations[4] = 4


for i in range(5,101):
	summations[i] = summations[i-1]+4
	print i, summations[i]


