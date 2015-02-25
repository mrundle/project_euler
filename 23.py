from math import sqrt
import time

# Sums proper divisors
def sum_divisors(n):
  sum_div = 1 # start with 1, because it is a divisor
  div = []
  sqrt_n = int(sqrt(n)) + 1
  for i in range(2,sqrt_n):
    if n % i == 0:
      sum_div += i
      sum_div += n/i
      print i, n/i
  return sum_div

def ret_abundant(limit):
  abundant = []  
  for i in range(1, limit + 1):
    if i < sum_divisors(i):
      abundant.append(i)
  return abundant

if __name__ == "__main__":

  print sum_divisors(12)
  #print ret_abundant(55)
  exit()

  ab_sums = [False] * (28123 + 1)
  abundant = ret_abundant(28123)
  for i in abundant:
    for j in abundant:
      if i + j > 28123: break
      else: ab_sums[i + j] = True
  sum = 0
  for i in range(28123 + 1):
    if ab_sums[i] == False: sum += i
  print sum
