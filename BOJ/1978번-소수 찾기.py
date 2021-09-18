# Create prime number list less than 1000
prime_numbers = []
for target_num in range(1, 1000):
  cnt = 0
  for div_num in range(1, target_num+1):
    if target_num % div_num == 0:
      cnt += 1
  if cnt == 2: # only if divided 1 and ifself
    prime_numbers.append(target_num)

# Input parameters
N = int(input())
input_numbers = [int(n) for n in input().split()]
ans = 0
assert len(input_numbers) == N

# Count prime numbers
for num in input_numbers:
  if num in prime_numbers:
    ans += 1

print(ans)
