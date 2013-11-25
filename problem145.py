# There are 120 reversible numbers below one-thousand. How many reversible numbers are there below one-billion (109)?

def r(n):
	k = [i for i in str(n)]
	return int("".join([k[len(k)-1-i] for i in range(0,len(k))]))

i = 0
k = 0
while i < 1000000000:
	u = True
	for h in str(i + r(i)):
		if int(h) % 2 == 0:
			u = False
	if u:
		k += 1
	i += 1
print k

# ==> 608720