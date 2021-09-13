# function for checking group word
def check_word(word):
  dist_w = [word[0]]
  ans = 1
  for n in range(len(word)-1):
    check = 0
    if word[n] != word[n+1]:
      check = 1
    else:
      check = 0
    if check == 1:
      if word[n+1] not in dist_w:
        dist_w.append(word[n+1])
      else:
        ans = 0
  return ans

# input N & word
N = int(input())
ans = 0
for n in range(N):
  word = input()
  ans += check_word(word)

print(ans)
