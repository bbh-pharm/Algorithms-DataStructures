# Function for checking primality
def primality(n):
  i = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += 1
  return True

# Create prime number list
prime_list = []
for n in range(2, 123456*2+1):
  if primality(n) == True:
    prime_list.append(n)

# Loop until input number is zero
n = int(input())
while n != 0:
  # Count prime numbers
  cnt = 0
  for prime_num in prime_list:
    if n < prime_num <= 2*n:
      cnt += 1
  print(cnt)
  n = int(input())
