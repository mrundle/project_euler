# Project Euler
# Problem 14
#
# Largest Collatz sequence

import time

def size_collatz(n):
  size = 1
  while n > 1:
    if n % 2 == 0:
      n = n/2
    else:
      n = 3*n + 1
    size += 1
  return size

if __name__ == "__main__":
  start = time.clock()
  max_size = 0
  max_num = 0
  for i in xrange(1000000):
    new_size = size_collatz(i)
    if new_size > max_size:
      max_size = new_size
      max_num = i
  elapsed = time.clock() - start
  print max_num, "(" + str(elapsed) + "s)"
