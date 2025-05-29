def isprime(num):
  
  if num < 2:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def findtwodigitprimes():
 
  primes = []
  for num in range(10, 100):
    if isprime(num):
      primes.append(num)
  return primes


twodigitprimes = findtwodigitprimes()
print("The two-digit prime numbers are:", twodigitprimes)