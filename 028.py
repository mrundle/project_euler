# ProjectEuler.net
# Problem 28
#
# Sum
def spiral_sum(dimension):
  curr = 1
  total = 1
  to_add = 0
  for i in range( (dimension - 1) / 2):
    to_add += 2
    for j in range(1,4+1):
      curr += to_add
      total += curr
  print total

if __name__ == "__main__":
  spiral_sum(1001)


