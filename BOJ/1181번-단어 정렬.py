words = []
N = int(input())
for n in range(N):
  words.append(input())
words = sorted([(len(w), w) for w in set(words)])
for n, w in words:
  print(w)
