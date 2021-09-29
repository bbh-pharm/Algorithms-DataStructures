import sys

N = int(input())
counting_array = [0]*(10001)

for n in range(N):
  counting_array[int(sys.stdin.readline())] += 1

for idx in range(10001):
  if counting_array[idx] != 0:
    for _ in range(counting_array[idx]):
      print(idx)
