a = 0
i = 2
while True:
	h = [int(e) for e in str(i)]
	j = [int(e) for e in str(i*2)]
	w = [int(e) for e in str(i*3)]
	q = [int(e) for e in str(i*4)]
	f = [int(e) for e in str(i*5)]
	g = [int(e) for e in str(i*6)]
	h.sort()
	j.sort()
	w.sort()
	q.sort()
	f.sort()
	g.sort()
	if h == j and j == w and w == q and q == f and f == g:
		a = i
		break
	i += 1
print a

