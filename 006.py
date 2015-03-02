# Problem 6
# ProjectEuler.net
#
# Sum square difference

sum_squares = 0
sum = 0
for x in range(1, 101):
  sum_squares += x*x
  sum += x
print (sum*sum) - sum_squares