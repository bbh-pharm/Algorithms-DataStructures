def d(num):
  num = str(num)
  ans = sum([int(n) for n in num]) + int(num)
  return ans

def solve(range_num):
  result = list((set(i for i in range(1, range_num))) - (set(d(n) for n in range(1, range_num))))
  return sorted(result)

for n in solve(10000):
  print(n)
