# Find the 100 000 000th squarefree fibonacci number.

from math import *
def sqr(n):
	if n != 1 and sqrt(n)%1 == 0:
		return True
	return False
def div(number):
        i=2
        d = []
        while i<number:
        	if number % i == 0:
        		d.append(i)
        	i+=1
        return d
f = [1,1]
y = 2
while True:
	j = f[0]+f[1]
	f[0] = f[1]
	f[1] = j
	u = True
	for i in div(j):
		if sqr(i):
			u = False
	if u == True:
		y+=1
	if y == 100000000:
		a = y
		break
print a