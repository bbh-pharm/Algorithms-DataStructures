# N은 0보다 크거나 같고, 99보다 작거나 같은 정수
N = input()
assert 0 <= int(N) <= 99
if int(N) < 10:
    N = '0' + N[0]
iter = 0; ans = N
while True:
  iter += 1
  N = N[1] + str(int(N[0]) + int(N[1]))[-1]
  if N == ans:
    print(iter)
    break
