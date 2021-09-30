from collections import Counter
import sys

N = int(input())
numbers = []

for n in range(N):
  numbers.append(int(sys.stdin.readline()))

cnt = Counter(numbers)

# Average
print(round(sum(numbers) / len(numbers)))
# Median
print(sorted(numbers)[len(numbers) // 2])
# Mode
maximum = cnt.most_common()[0][1]
modes = []
for cnt in cnt.most_common():
  if cnt[1] == maximum:
    modes.append(cnt[0])
if len(modes) > 1:
  print(sorted(modes)[1])
else:
  print(modes[0])
# Range
print(max(numbers) - min(numbers))
