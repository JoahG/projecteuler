# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers.
l = []
for i in range(900, 1000):
	for j in range (900, 1000):
		d = str(i*j)
		p = []
		for t in range(0, len(d)):
			p.append(d[t])
		q = []
		for f in range(0,len(p)):
			q.append(p[(len(p)-1)-f])
		if p == q:
			l.append(i*j)
a = l[len(l)-1]
print a
# ==> 906609