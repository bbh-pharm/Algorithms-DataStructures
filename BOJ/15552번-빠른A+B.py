import sys

iter = int(input())
for i in range(iter):
  a, b = map(int, sys.stdin.readline().split())
  assert 1 <= a <= 1000 and 1 <= b <= 1000
  print(a + b)
