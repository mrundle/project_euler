# Project Euler
# Problem 35

def primes_sieve(limit):
  primes = set()
  a = [True] * limit
  a[0] = a[1] = False
  for i, isprime in enumerate(a):
    if isprime == True:
      primes.add(i)
      for n in range(i*i, limit, i):
        a[n] = False
  return primes

if __name__ == "__main__":
  # Get a set of the primes < one mil
  primes = primes_sieve(1000000)
  
  # Check if rotations of primes are also prime
  count = 0
  for prime in primes:
    circ_prime = True
    sprime = str(prime)
    for i in range(len(sprime)):
      check = int(sprime[i:] + sprime[:i])
      if check not in primes:
        circ_prime = False
        break
    if circ_prime:
      count += 1

  print count