# Project Euler
# Problem 23

from math import sqrt
import time

# Sums proper divisors
def sum_divisors(n):
  sum_div = 1 # start with 1, because it is a divisor
  div = []
  sqrt_n = int(sqrt(n))
  for i in range(2,sqrt_n + 1):
    if n % i == 0:
      sum_div += i
      if (n/i) != i: sum_div += n/i
  return sum_div

def ret_abundant(limit):
  abundant = []  
  for i in range(1, limit + 1):
    if i < sum_divisors(i):
      abundant.append(i)
  return abundant

if __name__ == "__main__":
  start = time.time()
  limit = 28123
  ab_sums = [False] * (limit + 1)

  abundant = ret_abundant(limit + 1)

  for i in abundant:
    for j in abundant:
      if i + j > limit: break
      else: ab_sums[i + j] = True

  sum = 0
  for i, ab_sum in enumerate(ab_sums):
    if not ab_sum: sum += i

  elapsed = time.time() - start

  print sum, "(" + str(elapsed) + "s)"
