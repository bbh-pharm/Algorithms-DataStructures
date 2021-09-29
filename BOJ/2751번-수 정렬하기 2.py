import sys

N = int(input())
numbers = []
for n in range(N):
  numbers.append(int(sys.stdin.readline()))

numbers.sort()
for num in numbers:
    print(num)
