# Project Euler
# Problem 25
#
# 1000 digit Fibonacci number

if __name__ == "__main__":
  a = 1
  b = 1
  tmp = 0
  terms = 2
  while len(str(b)) < 1000:
    tmp = a + b
    a = b
    b = tmp
    terms += 1
  print terms
