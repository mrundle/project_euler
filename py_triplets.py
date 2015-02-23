# Problem 9
# ProjectEuler.net
#
# Special Pythagorean triplet

def gen_triples(limiting_sum):
  m, n = 0
  
  print m, n

def gen_fib(limit):
  fib = {}
  fib[1] = 0
  fib[2] = 1
  idx = 3
  while len(fib) <= limit:
    fib[idx] = fib[idx - 1] + fib[idx - 2]
    idx += 1
  return fib

if __name__ == "__main__":
  #gen_triples(1000)
  u_limit = 100 # upper limit on pairs of triples to check
  F = gen_fib(2 * u_limit) # the highest fibonacci number we'll need
  
  triples = {}
  triples[3] = [ 4, 3, 5 ]
  for i in range(4, 10 + 1):
    a = triples[i - 1][0] + triples[i - 1][1] + triples[i - 1][2]
    b = F[(2*i) - 1] - triples[i-1][1]
    c = F[2*i]
    triples[i] = [a, b, c]
    print "prod: ", a*b*c
