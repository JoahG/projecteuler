# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

def isPan(n):
	
	# Added specifically for this problem
	if not len(n) == 9:
		return False

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

arr = []

for i in range(1,99999):
	y = str(i)
	j = 2
	while len(y) < 9:
		y += str(i*j)
		j += 1
	if isPan(y):
		arr.append(y)

print arr[-1]