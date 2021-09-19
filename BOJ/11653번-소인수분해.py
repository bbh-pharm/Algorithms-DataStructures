# Input number
N = int(input())

# Loop until remainder = 1
while N != 1:
  n = 1
  while True:
    n += 1
    if N % n == 0:
      N /= n
      print(n)
      break
