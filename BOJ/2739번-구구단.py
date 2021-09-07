# N은 1보다 크거나 같고, 9보다 작거나 같다.
N = int(input())
assert 1 <= N <= 9

for i in range(1, 10):
  print(f"{N} * {i} = {N * i}")
