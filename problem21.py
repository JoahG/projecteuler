# Evaluate the sum of all the amicable numbers under 10000.

import time
start_time = time.time()

def d(n):
	i = 1
	t = []
	while i < n:
		if n % i == 0:
			t.append(i)
		i += 1
	return sum(t)

def valInList(a,i):
	try:
		a.index(i)
		return True
	except:
		return False

i = 1
dic = {}
while i < 10000:
	dic[i] = d(i)
	i += 1

l = []

for i in dic:
	for j in dic:
		if i != j and dic[i] == j and dic[j] == i and not valInList(l,i) and not valInList(l, j):
			l.append(i)
			l.append(j)

print l
print sum(l)
print time.time() - start_time, "seconds"