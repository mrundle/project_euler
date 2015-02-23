# Problem 8
# ProjectEuler.net
#
# Largest product in a series

def increment_idx(start_idx, end_idx, num_adj):
  if (end_idx - start_idx) < (num_adj - 1):
    end_idx += 1
  else:
    end_idx += 1
    start_idx += 1
  return start_idx, end_idx

def calculate_product(start_idx, end_idx, num_adj, input_str):
  product = 1
  for i in range(start_idx, end_idx + 1):
    product *= int(input_str[i])
  return product

def greatest_adj_prod(input_str, num_adj):
  greatest = 0
  curr_prod = 1
  start_idx = 0
  end_idx = 0
  done = False
  while not done:
    start_idx, end_idx = increment_idx(start_idx, end_idx, num_adj)
    if end_idx > (len(input_str) - 1):
      done = True
    elif input_str[end_idx] == 0:
      start_idx = end_idx + 1
      end_idx = start_idx
    elif (end_idx - start_idx) == (num_adj - 1):
      curr_prod = calculate_product(start_idx, end_idx, num_adj, input_str)
      if curr_prod > greatest:
        greatest = curr_prod
 
  return greatest
    
if __name__ == "__main__":
  input_str = '73167176531330624919225119674426574742355349194934' \
        '96983520312774506326239578318016984801869478851843' \
        '85861560789112949495459501737958331952853208805511' \
        '12540698747158523863050715693290963295227443043557' \
        '66896648950445244523161731856403098711121722383113' \
        '62229893423380308135336276614282806444486645238749' \
        '30358907296290491560440772390713810515859307960866' \
        '70172427121883998797908792274921901699720888093776' \
        '65727333001053367881220235421809751254540594752243' \
        '52584907711670556013604839586446706324415722155397' \
        '53697817977846174064955149290862569321978468622482' \
        '83972241375657056057490261407972968652414535100474' \
        '82166370484403199890008895243450658541227588666881' \
        '16427171479924442928230863465674813919123162824586' \
        '17866458359124566529476545682848912883142607690042' \
        '24219022671055626321111109370544217506941658960408' \
        '07198403850962455444362981230987879927244284909188' \
        '84580156166097919133875499200524063689912560717606' \
        '05886116467109405077541002256983155200055935729725' \
        '71636269561882670428252483600823257530420752963450' \
        
  print greatest_adj_prod(input_str,13)
  
