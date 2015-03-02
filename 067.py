# ProjectEuler.net
# Problem 67
# Identical solution (algorithm) to Problem 18

tri = []
f = open('p067_triangle.txt','r')
for line in f:
  tri.append([int(n) for n in (line.rstrip().split(' '))])
f.close()

for i in range(len(tri) - 1, 0, -1):
  for j in range(len(tri[i]) - 1):
    tri[i-1][j] += max(tri[i][j], tri[i][j+1])
print tri[0][0]