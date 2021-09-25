N = int(input())
step_list = []

def hanoi_tower(num, A, B, C):
  global step_list

  if num == 1:
    step_list.append((A, C))
  else:
    # step 1: A -> B (n-1)
    hanoi_tower(num - 1, A, C, B)
    # step 2: A -> C (1)
    step_list.append((A, C))
    # step 3: B -> C (n-1)
    hanoi_tower(num - 1, B, A, C)

hanoi_tower(N, 1, 2, 3)
print(len(step_list))
for step in step_list:
  start, end = step
  print(start, end)
