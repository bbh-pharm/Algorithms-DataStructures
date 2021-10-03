######################
## Using dictionary ##
######################
N = int(input())
num_list = list(map(int, input().split()))
answer_dict = {}
for idx, num in enumerate(sorted(list(set(num_list)))):
  answer_dict[num] = idx

for num in num_list:
  print(answer_dict[num], end=' ')
  
######################
## Using list index ##
######################
# This method takes a time limit
N = int(input())
num_list = list(map(int, input().split()))
sorted_list = sorted(list(set(num_list)))
for num in num_list:
  print(sorted_list.index(num), end=' ') # list method "index" needs N time complexity
  
 
