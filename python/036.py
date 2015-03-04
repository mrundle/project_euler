# ProjectEuler.net
# Problem 36
#
# Double-base palindromes
from math import pow

# Argument will set the upper limit for
# the palindromes
def base10_palindromes(pow_ten):
  palindromes = set()
  limit = int(pow(10,pow_ten))
  max_dig = len(str(limit)) - 1
  for digits in range(1,max_dig + 1):
    if digits == 1:
      for i in range(1,10):
        palindromes.add(i)
    if digits % 2 == 0:
      workable = digits / 2
      for i in range(1, int(pow(10,workable))):
        palindromes.add(int(str(i) + str(i)[::-1]))
    else:
      workable = (digits - 1) / 2
      for i in range(1, int(pow(10,workable))):
        for j in range(1,10):
          palindromes.add(int(str(i) + str(j) + str(i)[::-1]))
  return palindromes
  
def is_palindrome(test):
  test_len = 0
  if len(test) % 2 == 0: test_len = len(test) / 2
  else: test_len = (len(test) - 1) / 2
  for i in range(test_len):
    if test[i] != test[(len(test) - 1) - i]: return False
  return True

if __name__ == "__main__":
  b10_pals = base10_palindromes(6)
  sum = 0
  for p in b10_pals:
    if is_palindrome(bin(p)[2:]): sum += p
  print sum