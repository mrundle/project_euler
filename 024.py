# ProjectEuler.net
# Problem 24
# Lexicographical Permutations

from math import factorial



if __name__ == "__main__":
  nums = [0,1,2,3,4,5,6,7,8,9]
  perms = 1
  print len(nums)
  for i in range(1,len(nums)+1):
    perms *= i
    if perms >= 1000000:
      print i, perms
      break
  print perms
