# 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
while True:
  try:
    A, B = (int(n) for n in input().split())

    assert 0 < A <10 and 0 < B < 10
    print(A + B)
  except:
    break 
