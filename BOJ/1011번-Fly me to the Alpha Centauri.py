from math import ceil, sqrt

def centauri(x, y):
  diff = y - x
  temp = ceil(sqrt(diff))
  ans = temp * 2 - 1
  if (temp-1)**2 < diff <= temp*(temp-1):
    ans -= 1
  return ans  

T = int(input())
for t in range(T):
  x, y = map(int, input().split())
  print(centauri(x, y))
