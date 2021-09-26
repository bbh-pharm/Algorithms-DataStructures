def solve(target):
  result = []

  for num in range(1, target):
    next_num = sum([int(n) for n in list(str(num))]) + num
    if next_num == target:
      result.append(num)
  if result:
    return min(result)
  return 0

N = int(input())
print(solve(N))
