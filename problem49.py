from itertools import permutations as p
def per(n):
	return sorted(set([int("".join(list(i))) for i in list(p([i for i in str(n)]))]))

for i in range(1000,10000):
	for j in per(i):
		