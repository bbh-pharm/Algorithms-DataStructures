numbers = [int(n) for n in list(input())]
numbers.sort(reverse=True)
for n in numbers:
  print(n, end='')
