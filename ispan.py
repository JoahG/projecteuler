def isPan(n):
	a = True
	st = str(n)
	t = []
	for i in st:
		t.append(int(i))
	for i in range(1,len(t)+1):
		try:
			t.index(i)
		except:
			a = False
	return a