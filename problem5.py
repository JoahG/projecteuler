# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
l = []
p = [58773960*11*13*2*11*2]
for i in p:
	c = True
	for j in range(1,21):
		if i%j!=0:
			c = False
	if c == True:
		l.append(i)
		break
if len(l)>0:
	a = l[0]
	print a
else:
	print "none"

# ==> 232792560