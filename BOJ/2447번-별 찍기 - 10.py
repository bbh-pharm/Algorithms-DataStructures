N = int(input())
star_array = [[' ' for _ in range(N)] for _ in range(N)]

def star(n, x, y):
  global star_array

  if n == 3:
    star_array[x][y:y+3] = ['*', '*', '*']
    star_array[x+1][y:y+3] = ['*', ' ', '*']
    star_array[x+2][y:y+3] = ['*', '*', '*']
  else:
    next_size = n//3
    for dx in range(3):
      for dy in range(3):
        if dx != 1 or dy != 1:
          star(next_size, x + dx*next_size, y + dy*next_size)
  

star(N, 0, 0)
for i in star_array:
  print(''.join(i))
