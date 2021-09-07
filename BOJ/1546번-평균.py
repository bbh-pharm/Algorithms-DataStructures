# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 
# 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
N = int(input())
scores = [int(s) for s in input().split()]
assert len(scores) == N
cnt = 0
for score in scores:
  if score < 0 or 100 < score:
    raise ValueError
  else:
    if score > 0:
      cnt += 1
      
assert cnt != 0
max_score = max(scores)
avg_scores = []
for score in scores:
  score = score / max_score * 100
  avg_scores.append(score)

print(sum(avg_scores) / N)
