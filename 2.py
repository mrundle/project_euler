# returns sum of even fibonacci numbers
# under a max threshold (not including seeds)
def even_fibs(a, b, max):
  if a + b > max:
    return 0
  else:
    add = 0
    if (a + b) % 2 == 0:
      add = a + b
    return next_fib(b, a + b, max) + add

if __name__ == "__main__":
  upper_limit = 4000000
  # 2 must be added because the function doesn't include
  # seed values in its calculation
  print 2 + next_fib(1, 2, upper_limit)