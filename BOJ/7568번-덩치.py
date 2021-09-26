N  = int(input())
data = []
for n in range(N):
  data.append([int(i) for i in input().split()])
result = []

for wh in data:
  weight = wh[0]
  height = wh[1]
  cnt = 1
  for next_wh in [i for i in data if i != wh]:
    next_weight = next_wh[0]
    next_height = next_wh[1]
    if next_weight > weight and next_height > height:
      cnt += 1
  result.append(cnt)

for n in result:
  print(n, end=' ')
