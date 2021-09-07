# (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)
num = input().split()
H = int(num[0]); M = int(num[1])

assert 0 <= H <= 23 and 0 <= M <= 59

if M >= 45:
  M -= 45
else:
  if H != 0:
    H -= 1
    M += 15
  else:
    H = 23
    M += 15

print(H, M)
