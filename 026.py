# ProjectEulder.net
# Problem 26

def gen_dec_frac(n):
  decimals = []
  divisor = n
  denominator = 1
  # get the original division
  num_repeating = 0
  prev_pairs = [(0,0)]
  while True:
    leading_zeroes = 0
    
    while denominator < divisor:
      denominator *= 10
      leading_zeroes += 1
    if prev_pairs[0] == (0,0): 
      prev_pairs[0] = denominator, divisor
      num_repeating += leading_zeroes -1
      for i in range(leading_zeroes - 1):
        decimals.append(0)
    elif (denominator, divisor) in prev_pairs: break
    prev_pairs.append((denominator, divisor))
   
    tally = int(denominator / divisor)
    num_repeating += 1
    denominator = denominator % divisor
    decimals.append(tally)
    if denominator == 0: break
  return decimals
    
if __name__ == "__main__":
  max_d = 1000
  ans = 0
  ans_sum = 0
  for d in range(2,max_d + 1):
    tmp_sum = len(gen_dec_frac(d)) 
    if tmp_sum > ans_sum:
      ans = d
      ans_sum = tmp_sum
  print ans