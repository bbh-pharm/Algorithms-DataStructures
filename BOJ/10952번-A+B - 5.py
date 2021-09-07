# 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개
while True:
  A, B = (int(n) for n in input().split())

  if A == 0 and B == 0:
    break

  assert 0 < A <10 and 0 < B < 10
  print(A + B)
