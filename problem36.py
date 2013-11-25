# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# ******* Found Code Snippet on http://stackoverflow.com/questions/2267362/convert-integer-to-a-string-in-a-given-numeric-base-in-python *****
import string
digs = string.digits + string.lowercase

def int2base(x, base):
  if x < 0: sign = -1
  elif x==0: return '0'
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)
# End Code Snippet 

def isPal(n):
  if isinstance(n,int):
    n = str(n) 
  if len(n) <= 1:
    return True
  if n[0] == n[-1]:
    return isPal(n[1:-1])
  return False

y = 0
for i in range(1,1000001):
	if isPal(i) and isPal(int2base(i,2)):
		y += i
print y
# ==> 872187