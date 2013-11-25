
def isPentagonal(n):
	i = 0
	j = 0
	while j < n:
		j = i*(3*i-1)/2
		if j == n:
			return True
		i += 1
	return False

def satisfy(a, b):
	if isPentagonal(a) and isPentagonal(b) and isPentagonal(a+b) and isPentagonal(a-b):
		return True

j = 0
i = 1
while j < 1:
	print i
	for p in range(1,10000):
		if satisfy(i,p):
			print i
			print p
			j += 1
	i += 1