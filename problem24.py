# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

arr = []
x = range(0,10)
for a in x:
	print a
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
																			arr.append(int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)))
arr.sort()
print arr[999999]