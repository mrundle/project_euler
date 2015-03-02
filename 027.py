# ProjectEuler.net
# Problem 27

from math import sqrt, pow
import time

# Sums proper divisors
def is_prime(n):
    if n <= 1:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(2,sqrt_n + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
  start = time.clock()
  
  primes = {}
  max_len = 0
  max_pair = 0, 0
  max_a = 1000
  max_b = 1000
  for a in range((max_a * -1) + 1, max_a):
    for b in range((max_b * -1) + 1, max_b):
      n = 0
      primes = 0
      go = True
      while go:
        x = pow(n,2) + (a*n) + b
        if is_prime(x):
          n += 1
          primes += 1
          if primes > max_len:
            max_len = primes
            max_pair = a, b
        else:
          go = False
    
  elapsed = time.clock() - start
  
  print max_pair, "(", elapsed, "s)"