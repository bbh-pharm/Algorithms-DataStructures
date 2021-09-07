# N(1 ≤ N ≤ 100)
N = int(input())
assert 1 <= N <= 100
for n in range(N):
  print("*" * (n+1))
