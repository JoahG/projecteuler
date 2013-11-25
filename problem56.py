
arr = []
for i in range(1,100):
	for j in range(1,100):
		arr.append(sum([int(n) for n in str(i**j)]))
		
arr.sort()
print arr[-1]