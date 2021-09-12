chroatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
idx_list = []
for chro in chroatia_list:
  du_check = 0
  if chro in word:
    for i in range(len(word)):
      lidx = word.find(chro, du_check)
      ridx = word.find(chro, du_check)+len(chro)-1
      if lidx != -1:
        idx_list.append((lidx, ridx))
        du_check = word.find(chro, du_check)+len(chro)-1

# Remove duplicate index
idx_list.sort()
for i in range(len(idx_list)-1):
  try:
    if idx_list[i][1] >= idx_list[i+1][0]:
      del idx_list[i+1]
  except: pass

# Consider loger index
check = 0
for idx in idx_list:
  if idx[1] - idx[0] == 2:
    check +=1

# Append other index
temp = [x for idx_tuple in sorted(idx_list) for x in idx_tuple]
for n in range(len(word)):
  if n not in temp:
    idx_list.append(n)

print(len(idx_list)-check)
