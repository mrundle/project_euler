# Problem 4
# ProjectEuler.net
#
# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
  if str(n) == str(n)[::-1]:
    return True
  else:
    return False
    
def find_palindrome(a,b,num_dig):
  largest = 0
  while len(str(a)) == num_dig:
    while len(str(b)) == num_dig:
      if is_palindrome(a*b):
        if (a*b) > largest:
          largest = a*b
      b = b - 1
    a = a - 1
    b = a
  return largest
    
if __name__ == "__main__":
  print find_palindrome(999,999,3)