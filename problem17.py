import math

def spellNumber(n, z = False, p = False):
	for i in str(n):
		if i == ".":
			p = str(n).split(".")
			return spellNumber(int(p[0])) + spellNumber(int(p[1]), False, True)
	if p:
		o = " point "
		for i in str(n):
			o += spellNumber(int(i), True) + " "
		return o
	if n <= 19:
		o = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][n]
		if o == "zero" and z or o != "zero":
			return o
		return ""
	if n <= 99:
		if spellNumber(int(str(n)[-1])) != "zero":
			return ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][int(math.floor(n/10))-2] + "" + spellNumber(int(str(n)[-1]), False)
		return ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][int(math.floor(n/10))-2]
	if n <= 999:
		if n % 100 == 0:
			return spellNumber(int(math.floor(n/100))) + "hundred" + spellNumber(int(n-(math.floor(n/100)*100)))
		return  spellNumber(int(math.floor(n/100))) + "hundredandr" + spellNumber(int(n-(math.floor(n/100)*100)))
	if n <= 999999:
		return spellNumber(int(math.floor(n/1000))) + "thousand" + spellNumber(int(n-(math.floor(n/1000)*1000)))
	if n <= 9999999999999999999999999999999:
		if len(str(n)) >= 7 and len(str(n)) <= 9:
			return spellNumber(int(math.floor(n/1000000))) + " million " + spellNumber(int(n-(math.floor(n/1000000)*1000000)))
		if len(str(n)) >= 10 and len(str(n)) <= 12:
			return spellNumber(int(math.floor(n/1000000000))) + " billion " + spellNumber(int(n-(math.floor(n/1000000000)*1000000000)))
		if len(str(n)) >= 13 and len(str(n)) <= 15:
			return spellNumber(int(math.floor(n/1000000000000))) + " trillion " + spellNumber(int(n-(math.floor(n/1000000000000)*1000000000000)))
		if len(str(n)) >= 16 and len(str(n)) <= 18:
			return spellNumber(int(math.floor(n/1000000000000000))) + " quadrillion " + spellNumber(int(n-(math.floor(n/1000000000000000)*1000000000000000)))
		if len(str(n)) >= 19 and len(str(n)) <= 21:
			return spellNumber(int(math.floor(n/1000000000000000000))) + " pentillion " + spellNumber(int(n-(math.floor(n/1000000000000000000)*1000000000000000000)))
		if len(str(n)) >= 22 and len(str(n)) <= 24:
			return spellNumber(int(math.floor(n/1000000000000000000000))) + " sextillion " + spellNumber(int(n-(math.floor(n/1000000000000000000000)*1000000000000000000000)))
		if len(str(n)) >= 25 and len(str(n)) <= 27:
			return spellNumber(int(math.floor(n/1000000000000000000000000))) + " septillion " + spellNumber(int(n-(math.floor(n/1000000000000000000000000)*1000000000000000000000000)))
		if len(str(n)) >= 28 and len(str(n)) <= 30:
			return spellNumber(int(math.floor(n/1000000000000000000000000000))) + " octillion " + spellNumber(int(n-(math.floor(n/1000000000000000000000000000)*1000000000000000000000000000)))
		if len(str(n)) >= 31 and len(str(n)) <= 33:
			return spellNumber(int(math.floor(n/1000000000000000000000000000000))) + " noventillion " + spellNumber(int(n-(math.floor(n/1000000000000000000000000000000)*1000000000000000000000000000000)))

i = 1
t = 0


while i <= 1000:
	print spellNumber(i)
	t += len(spellNumber(i))
	i += 1

print t