# 첫째 줄에 테스트 케이스의 개수
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열
iter = int(input())
for i in range(iter):
  ans = input()
  ans_list = [word for word in ans]; assert 0 < len(ans_list) < 80
  score_list = []  
  cnt = 0
  for w in ans_list:
    if w == 'O':
      cnt += 1
    elif w == 'X':
      cnt = 0
    else:
      raise ValueError
    score_list.append(cnt)
  print(sum(score_list))
