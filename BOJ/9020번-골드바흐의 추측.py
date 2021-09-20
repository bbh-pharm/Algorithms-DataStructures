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
for n in range(2, 10000):
  if primality(n) == True:
    prime_list.append(n)

# Input T: iteration
T = int(input())
for t in range(T):
  n = int(input())
  # Check from the middle
  max_num = 0
  for prime_num in prime_list:
    if prime_num <= n/2:
      max_num = prime_num
    else:
      break
  # Loop for finding prime numbers
  A, B = 0, 0
  while A + B != n:
    max_idx = prime_list.index(max_num)
    A = max_num
    if (n-A) in prime_list:
      B = n-A
      print(A, B)
    else:
      max_idx -= 1
      max_num = prime_list[max_idx]
