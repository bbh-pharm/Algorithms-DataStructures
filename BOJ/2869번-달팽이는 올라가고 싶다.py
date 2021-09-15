from math import ceil

A, B, V = map(int, input().split())

assert A != B
cnt = ceil((V-A) / (A-B))
print(cnt+1)
