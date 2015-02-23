# Problem 5
# ProjectEuler.net

# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by 
# all of the numbers from 1 to 20?
#
# Conceptual help: http://codereview.stackexchange.com/questions/13086/problem-5-on-project-euler

import math # only used for the pow function

def get_factors(n, all_factors):
  factors = {}
  while n > 1:
    used_a_factor = False
    for factor in all_factors:
      if n % factor == 0:
        n /= factor
        if factor in factors:
          factors[factor] += 1
        else:
          factors[factor] = 1
        used_a_factor = True
    if not used_a_factor:
      factors[n] = 1
      return factors
  return factors
  
if __name__ == "__main__":
  all_factors = {}
  top_range = 20
  for n in range(2,top_range + 1):
    factors = get_factors(n, all_factors)
    for factor in factors:
      if factor not in all_factors:
        all_factors[factor] = 1
      else:
        if factors[factor] > all_factors[factor]:
          all_factors[factor] = factors[factor]
  
  answer = 1
  for factor in all_factors:
    answer *= math.pow(factor, all_factors[factor])
  print int(answer)