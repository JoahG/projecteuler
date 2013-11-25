
g = 15499.0/94744.0

def r(n):
	r = n-1
	t = 0
	for i in range(1,int(n)):
		b = True
		for j in range(2, i+1):
			if n % j == 0 and i % j == 0:
				b = False
				break
		if b:
			t += 1
	return float(t)/float(r)

i = 892371480.0
while r(i) >= g:
	i += 1.0
print i