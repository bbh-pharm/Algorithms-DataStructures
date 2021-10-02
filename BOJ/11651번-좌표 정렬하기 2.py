import sys

points = []
N = int(input())
for n in range(N):
  x, y = map(int, sys.stdin.readline().split())
  points.append((y, x))
points.sort()
for y, x in points:
  print(x, y)
