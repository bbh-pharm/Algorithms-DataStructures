# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수
num_list = []
for i in range(3):
  num = int(input())
  assert 100 <= num < 1000
  num_list.append(num)
A = num_list[0]; B = num_list[1]; C = num_list[2]
product = str(A * B * C)

product_split_list = [product[i] for i in range(len(product))]
for n in range(10):
  count = 0
  for i in range(len(product_split_list)):
    if product_split_list[i] == str(n):
      count += 1
  print(count)
