answer_b = []
answer_w = []
for i in range(4):
  answer_b.append(list('BWBWBWBW'))
  answer_b.append(list('WBWBWBWB'))
for j in range(4):
  answer_w.append(list('WBWBWBWB'))
  answer_w.append(list('BWBWBWBW'))

N, M = map(int, input().split())

board = []
for n in range(N):
  board.append(list(input()))

ans = []
for n in range(N - 8 + 1):
  for m in range(M - 8 + 1):
    same_b = 0
    same_w = 0
    crop_board = []
    for i in board[n: n+8]:
      crop_board.append(i[m:m+8])

    for i in range(8):
      for j in range(8):
        if crop_board[i][j] == answer_b[i][j]:
          same_b += 1
        if crop_board[i][j] == answer_w[i][j]:
          same_w += 1
  
    ans.append(min(same_b, same_w))

print(min(ans))
