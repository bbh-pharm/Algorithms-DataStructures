N = int(input())
ori_N = N
ans = -1

if N % 5 == 0:
  ans = N//5
else:
  cnt = 0
  for n in range(N):
    N -= 3
    cnt += 1
    if N % 5 == 0:
      ans = cnt + (ori_N-cnt*3) // 5
      break
    elif N <= 0:
      break

print(ans)
