# 첫째 줄에는 테스트 케이스의 개수 C
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수
# 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력
C = int(input())
for c in range(C):
  num_list = [int(n) for n in input().split()]
  N = num_list[0]; assert 1 <= N <= 1000
  score_list = num_list[1:]
  # make error in invalid score
  for score in score_list:
    if score < 0 or score > 100:
      raise ValueError
  # compute average and print ratio
  avg_score = sum(score_list) / len(score_list)
  cnt = 0
  for score in score_list:
    if score > avg_score:
      cnt += 1
  print("{:.3f}%".format(round(cnt / len(score_list) * 100, 3)))
