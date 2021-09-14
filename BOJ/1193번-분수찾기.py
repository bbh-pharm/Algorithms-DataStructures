a = int(input())
i = 1; j = 1
while i < a:
  j += 1
  i += j
num_in_group = a - (i - j + 1) + 1
if j % 2 == 1:
  print(f'{j+1-num_in_group}/{num_in_group}')
else:
  print(f'{num_in_group}/{j+1-num_in_group}')
