# ProjectEuler.net
# Problem 29
#
from math import pow

def distinct_pow(n):
  pows = set()
  for i in range(2,n+1):
    for j in range(2,n+1):
      power = pow(i,j)
      if power not in pows:
        pows.add(power)
  return len(pows)

if __name__ == "__main__":
  print distinct_pow(100)