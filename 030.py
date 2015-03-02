# ProjectEuler.net
# Problem 30
#
# Digit fifth powers
from math import pow
ubound = int(6 * pow(9,5))
tot_sum_powers = 0
for i in range(2,ubound):
  sum_powers = 0
  num = str(i)
  for j in range(len(num)):
    sum_powers += pow(int(num[j]),5)
  if sum_powers == i:
    tot_sum_powers += sum_powers
print int(tot_sum_powers)
