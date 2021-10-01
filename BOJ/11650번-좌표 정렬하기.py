import sys

points = []
N = int(input())
for n in range(N):
  x, y = map(int, sys.stdin.readline().split())
  points.append((x, y))
points.sort()
for x, y in points:
  print(x, y)
