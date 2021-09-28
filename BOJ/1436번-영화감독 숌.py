N = int(input())
n = 0
cnt = 0
while True:
  n += 1 
  if '666' in str(n):
    cnt += 1
  if cnt == N:
    print(n)
    break
