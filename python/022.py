# Project Euler
# Problem 22
# 
# Names scores
import time

def name_to_value(name):
  val = 0  
  for c in name:
    val += ord(c) - 64
  return val

if __name__ == "__main__":
  start = time.time()

  f = open('../files/p022_names.txt','r')
  content = f.readline()
  f.close()

  names = sorted(content.replace('"','').split(','))

  total = 0
  for i, name in enumerate(names):
    total += (name_to_value(name) * (i + 1))
  
  elapsed = time.time() - start  
  print total, "(" + str(elapsed) + "s)"
