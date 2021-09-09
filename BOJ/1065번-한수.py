# 1,000보다 작거나 같은 자연수 N

# to calculate substrattion of element of number
def cal_sub(number):
  input_list = [int(n) for n in str(number)]
  result = []
  if len(input_list) == 1:
    return result
  else:
    for n in range(len(input_list)-1):
      result.append(input_list[n+1] - input_list[n])
    return result

# input numbers
N = int(input())
assert 1 <= N <= 1000
cnt = 0

for n in range(1, N+1):
  sub_list = cal_sub(n)
  if sub_list:
    t = 0
    for sub in sub_list:
      if sub == sub_list[0]:
        t += 1
    if t == len(sub_list):
      cnt += 1
  else:
    cnt += 1

print(cnt)

###################################
## 자리수가 명확하기 때문에 참고 ##
###################################

def hansu(num) :
    hansu_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            hansu_cnt += 1  # 100보다 작으면 모두 한수
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
    return hansu_cnt

num = int(input())
print(hansu(num))
