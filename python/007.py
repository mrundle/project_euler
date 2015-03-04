# Problem 7
# ProjectEuler.net
#
# 10001st prime

def is_prime(n, primes):
  for i in primes:
    if n % i == 0:
      return False
  return True

prime = 2
n_prime = 1
t_prime = 10001
primes = []

while n_prime != t_prime:
  prime += 1
  if is_prime(prime,primes):
    n_prime += 1
    primes.append(prime)

print prime