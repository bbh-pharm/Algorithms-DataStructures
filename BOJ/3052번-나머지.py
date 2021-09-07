# 숫자는 1,000보다 작거나 같고, 음이 아닌 정수
re_list = []
cnt = 0
for i in range(10):
  num = int(input())
  assert 0 <= num <= 1000
  remain = num % 42
  if remain not in re_list:
    re_list.append(remain)
    cnt += 1

print(cnt)
