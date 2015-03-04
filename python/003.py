# Problem 3
# ProjectEuler.net
#
# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(n):
  idx = 2
  while idx < n:
    if n % idx == 0:
      return largest_prime_factor(n / idx)
    else:
      idx += 1
  return n
  
if __name__ == "__main__":
  target = 600851475143
  print largest_prime_factor(target)