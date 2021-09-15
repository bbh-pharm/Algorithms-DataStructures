T = int(input())
for t in range(T):
  H, W, N = map(int, input().split())
  h = str(N % H)
  if int(h) == 0:
    h = str(H)
  w = str(N // H + 1)
  if N % H == 0:
    w = str(N // H)
  if int(w) < 10:
    w = "0"+w
  print(h+w)
