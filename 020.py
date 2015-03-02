# Project Euler
# Problem 20
#
# Factorial digit sum

factorial = 1
for i in range(1,101):
  factorial *= i
sum_factorial = 0
for i in str(factorial):
  sum_factorial += int(i)
print sum_factorial
