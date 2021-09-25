#################
## Brute-force ##
#################

N, M = map(int, input().split())
num_list = [int(n) for n in input().split()]
sum_list = []

for i in num_list:
  for j in num_list[num_list.index(i)+1:]:
    for k in num_list[num_list.index(j)+1:]:
      if i + j + k <= M:
        sum_list.append(i+j+k)

print(max(sum_list))

#####################
## Using itertools ##
#####################
from itertools import combinations 

N, M = map(int, input().split())
num_list = [int(n) for n in input().split()]

ans = 0 
for tmp in combinations(num_list, 3): 
  if ans == M: 
    break 
  elif sum(tmp) > ans and sum(tmp) <= M: 
    ans = sum(tmp) 

print(ans)
