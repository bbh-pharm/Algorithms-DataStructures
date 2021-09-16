T = int(input())

first = [i for i in range(1, 15)]
result = [first]
for i in range(14):
  temp = []
  for j in range(1, 15):
    temp.append(sum(result[i][:j]))
  result.append(temp)

for t in range(T):
  k = int(input()); n = int(input())
  print(result[k][n-1])
