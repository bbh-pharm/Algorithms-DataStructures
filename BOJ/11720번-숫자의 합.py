# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
N = int(input())
assert 1 <= N <= 100
number = input()
assert len(number) == N

num_list = [int(n) for n in number]
print(sum(num_list))
