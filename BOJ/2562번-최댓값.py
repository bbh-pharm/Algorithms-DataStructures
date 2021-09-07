# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
num_list = []
for i in range(9):
  num = int(input())
  assert 0<= num < 100
  num_list.append(num)

print(max(num_list))
print(max(range(len(num_list)), key = (lambda x: num_list[x])) + 1)
