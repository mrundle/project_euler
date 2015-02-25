# Project Euler
# Problem 21
# 
# Amicable numbers
from math import sqrt
import time

def sum_divisors(n):
  sum_div = 1 # start with 1, because it is a divisor
  div = []
  sqrt_n = int(sqrt(n)) + 1
  for i in range(2,sqrt_n):
    if n % i == 0:
      sum_div += i
      sum_div += n/i
  return sum_div

if __name__ == "__main__":

  start = time.time()

  sum_div = {}

  for i in range(1,10000):
    sum_div[i] = sum_divisors(i)
  amicable = []

  for n in range(1,10000):
    if sum_div[n] < len(sum_div):
      if sum_div[sum_div[n]] == n and n != sum_div[n]:
        if n not in amicable: amicable.append(n)
        if sum_div[n] not in amicable: amicable.append(sum_div[n])

  elapsed = time.time() - start

  print sum(amicable), "(" + str(elapsed) + "s)"
