# Problem 10
# ProjectEuler.net
#
# Summation of primes

# Sieve of Eratosthenese: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Help: http://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
def primes_sieve(limit):
  primes = []
  a = [True] * limit
  a[0] = a[1] = False
  for i, isprime in enumerate(a):
    if isprime == True:
      primes.append(i)
      for n in xrange(i*i, limit, i):
        a[n] = False
  return primes
  
if __name__ == "__main__":
  limit = 2000000
  primes = primes_sieve(limit)
  summation = 0
  for prime in primes:
    summation += prime
  print summation
  
