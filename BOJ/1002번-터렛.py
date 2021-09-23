from math import sqrt

T = int(input())
for t in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  dist = sqrt((x1- x2)**2 + (y1 - y2)**2)
  if x1 == x2 and y1 == y2 and r1 == r2:
    print(-1)
  else:
    if (dist == r1+ r2) or (r1 == dist + r2) or (r2 == r1 + dist):
      print(1)
    else:
      t = sorted([r1, r2, dist])
      if t[-1] > t[0] + t[1]:
        print(0)
      else:
        print(2)
