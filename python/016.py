# Project Euler
# Problem 16
#
# Power digit sum
import time
start = time.clock()
n = str(pow(2,1000))
nsum = 0
for i in n:
  nsum += int(i)
elapsed = time.clock() - start
print nsum, "(" + str(elapsed) + "s)"
