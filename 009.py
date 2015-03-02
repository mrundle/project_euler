# Problem 9
# ProjectEuler.net
#
# Special Pythagorean triplet
import math

def gen_triples(target_sum):
  b = 0
  while True:
    b += 1
    for a in range (1, b):
      c = math.sqrt((a**2) + (b**2))
      if a + b + c == target_sum:
        return int(a), int(b), int(c)


if __name__ == "__main__":
  product = 1
  for n in gen_triples(1000):
    product *= n
  print product
