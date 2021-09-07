# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수
N, X = (int(i) for i in input().split())
A = [int(a) for a in input().split()]

assert 1 <= N <= 10000 and 1 <= X <= 10000
assert len([n for n in A if 1 <= n <= 10000]) == N

ans = [n for n in A if n < X]
for i in ans:
  if ans:
    print(i, end=' ')
  else:
    raise ValueError
