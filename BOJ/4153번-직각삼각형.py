def is_right(num_list):
  max_num = max(num_list)
  num_list.sort()
  if max_num**2 == (num_list[0]**2 + num_list[1]**2):
    ans = "right"
  else:
    ans = "wrong"
  return ans

input_num = [int(n) for n in input().split()]
while input_num != [0, 0, 0]:
  print(is_right(input_num))
  input_num = [int(n) for n in input().split()]
