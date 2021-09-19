# Function for primality identification
def primality(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Input parameters
M, N = map(int, input().split())

# Check numbers
for n in range(M, N+1):
  if primality(n) == True and n != 1:
    print(n)
