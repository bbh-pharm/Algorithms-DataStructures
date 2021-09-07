# 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
x = int(input())
y = int(input())

assert -1000 <= x <= 10000 and x != 0
assert -1000 <= y <= 10000 and x != 0

ans = 0 
if x > 0:
  ans = (1 if y > 0 else 4)
else:
  ans = (2 if y > 0 else 3)

print(ans)
