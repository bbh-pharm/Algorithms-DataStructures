from math import floor

A, B, C = [int(n) for n in input().split()]
try:
  x = floor(A / (C-B) + 1)
except:
  x = -1
if x <= 0:
  x = -1
print(x)
