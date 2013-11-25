
from itertools import permutations as p
from math import pow

def is_cube(n):
    root = pow(n, 1.0/3.0)
    if int(pow(round(root),3)) == n: 
        return True
    return False

def per(n):
	return [int("".join(list(i))) for i in list(p([i for i in str(n)]))]

i = 345

while True:
	q = []
	for j in per(int(pow(i,3))):
		if is_cube(j):
			try:
				q.index(j)
			except:
				q.append(j)
	if len(q) == 5:
		print i, len(q)
		break
	if len(q) >= 3:
		print i, q
	i += 1