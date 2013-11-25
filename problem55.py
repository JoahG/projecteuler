# How many Lychrel numbers are there below ten-thousand?
import time
start_time = time.time()

def isPal(n):
	if str(n) == str(n)[::-1]:
		return True
	return False

def isLychrel_helper(n):
	q = n+int(str(n)[::-1])
	if isPal(q):
		return False
	return q

def isLychrel(n):
	t = n
	i = 1
	while isLychrel_helper(t) and i <= 50:
		t = isLychrel_helper(t)
		i += 1
		if i == 50:
			return True
	return False


i = 0
for j in range(1,10001):
	if isLychrel(j):
		i += 1
	j += 1

print i
print time.time() - start_time, "seconds"