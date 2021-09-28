N = int(input())
numbers = []
for n in range(N):
  numbers.append(int(input()))

numbers.sort()
for n in numbers:
  print(n)
