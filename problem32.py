# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

def isPan(n):
	a = True
	st = str(n)
	t = []
	for i in st:
		t.append(int(i))
	for i in range(1,len(t)+1):
		try:
			t.index(i)
		except:
			a = False
	return a

answer = []
for i in range(1,2001):
	for j in range(1,2001):
		ij = str(i)+str(j)+str(i*j)
		if len(ij) == 8 and isPan(ij):
			try:
				answer.index(i*j)
			except:
				print i, "X", j, "=", i*j
				answer.append(i*j)

answer = sum(answer)
print answer