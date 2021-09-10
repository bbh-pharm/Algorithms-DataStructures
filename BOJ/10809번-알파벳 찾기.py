def get_words(word):
  word_list = list(word)
  a_z_list = [chr(asc) for asc in range(ord('a'), ord('z')+1)]
  for a in a_z_list:
    if a in word_list:
      ans = word_list.index(a)
    else:
      ans = -1
    print(ans, end=' ')

S = input()
get_words(S)
