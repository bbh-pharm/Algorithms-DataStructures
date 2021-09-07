# n (1 ≤ n ≤ 10,000)
num = int(input())
assert 1 <= num <= 10000

result = 0
for n in range(1, num+1):
  result += n
print(result)
