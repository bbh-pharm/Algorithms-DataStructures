N = int(input())
i = 1
j = 0
cnt = 0
while j < N:
  j += i
  if i != 1:
    i += 6
  else:
    i *= 6
  cnt += 1

print(cnt)
