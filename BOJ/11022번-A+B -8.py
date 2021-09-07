#  (0 < A, B < 10)
# "Case #x: A + B = C"
T = int(input())

for n in range(T):
  num_list = [int(num) for num in input().split()]
  A = num_list[0]; B = num_list[1]
  assert 0 < A < 10 and 0 < B < 10

  print(f"Case #{n+1}: {A} + {B} = {A + B}")
