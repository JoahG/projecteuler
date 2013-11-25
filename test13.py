def isPrime(number):
  if number%2 == 0:
      return False
  for p in range(3,int(number**0.5)+1,2):
          if number%p==0:
                  return False
  return True

print isPrime(157)