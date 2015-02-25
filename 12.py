# ProjectEuler.net
# Problem 12
#
# Highly divisible triangular number

from math import sqrt

def divisors(triangle_num):
  divisors = 0
  sqrt_num = int(sqrt(triangle_num))
  i = 0
  while i < sqrt_num:
    i += 1
    if triangle_num % i == 0: divisors += 2
  if sqrt_num * sqrt_num == triangle_num: divisors -= 1
  return divisors

if __name__ == "__main__":
  triangle_num = 0
  i = 1
  while divisors(triangle_num) < 500:
    triangle_num += i
    i += 1
    print triangle_num, divisors(triangle_num)

  print triangle_num