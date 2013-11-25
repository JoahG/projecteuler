# What is the only (double-digit or higher) Prime number that is palindromic in both Base-2 and Base-10 instances?

import string
digs = string.digits + string.lowercase
def isPrime(number):
  if number%2 == 0:
      return False
  for p in range(3,int(number**0.5)+1,2):
          if number%p==0:
                  return False
  return True
  
def isPal(n):
  if isinstance(n,int):
    n = str(n) 
  if len(n) <= 1:
    return True
  if n[0] == n[-1]:
    return isPal(n[1:-1])
  return False

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
u = 0
for i in range(11,1001):
  if isPrime(i) and isPal(i):
    u += 1
print u


# ==> 313