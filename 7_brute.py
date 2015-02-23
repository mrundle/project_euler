# Problem 7
# ProjectEuler.net
#
# 10001st prime
def is_prime(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

prime = 2
n_prime = 1
t_prime = 10001

while n_prime != t_prime:
  prime += 1
  if is_prime(prime):
    n_prime += 1

print prime