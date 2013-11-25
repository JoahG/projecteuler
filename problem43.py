def isPan(n):
	a = True
	st = str(n)

	#problem-specific
	if not len(st) == 10:
		return False

	t = []
	for i in st:
		t.append(int(i))
	for i in range(0,len(t)):
		try:
			t.index(i)
		except:
			a = False
	return a

def satisfy(n):
	st = str(n)
	if isPan(n) and int(st[1:4]) % 2 == 0 and int(st[2:5]) % 3 == 0 and int(st[3:6]) % 5 == 0 and int(st[4:7]) % 7 == 0 and int(st[5:8]) % 11 == 0 and int(st[6:9]) % 13 == 0 and int(st[7:10]) % 17 == 0:
		return True
	return False

t = 0
arr = []

x = range(0,10)
for a in x:
	for b in x:
		if b != a:
			for c in x:
				if c != b and c != a:
					for d in x:
						if d != c and d != b and d != a:
							for e in x:
								if e != d and e != c and e != b and e != a:
									for f in x:
										if f != e and f != d and f != c and f != b and f != a:
											for g in x:
												if g != f and g != e and g != d and g != c and g != b and g != a:
													for h in x:
														if h != g and h != f and h != e and h != d and h != c and h != b and h != a:
															for i in x:
																if i != h and i != g and i != f and i != e and i != d and i != c and i != b and i != a:
																	for j in x:
																		if j != i and j != h and j != g and j != f and j != e and j != d and j != c and j != b and j != a:
																			k = int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j))
																			if satisfy(k):
																				t += k
																				print k
		
print "total:", t