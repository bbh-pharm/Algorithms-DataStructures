# Input parameters
M = int(input())
N = int(input())

# Check prime numbers
prime_numbers = []
for target_num in range(M, N+1):
  cnt = 0
  for div_num in range(1, target_num+1):
    if target_num % div_num == 0:
      cnt += 1
  if cnt == 2: # only if divided 1 and ifself
    prime_numbers.append(target_num)

# Print answer
if prime_numbers:
  print(sum(prime_numbers))
  print(min(prime_numbers))
else:
  print(-1)
