# (0 < A, B < 10)
N = int(input())

for n in range(N):
  numbers = [int(n) for n in input().split()]
  A = numbers[0]; B = numbers[1]
  assert 0 < A < 10 and 0 < B < 10
  print(A + B)
