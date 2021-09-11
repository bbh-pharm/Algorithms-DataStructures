word = input()
def get_chrdict(word):
  chr_list = list(word.lower())
  unique_chr = []
  chr_dict = {}

  for character in chr_list:
    if character not in unique_chr:
      unique_chr.append(character)
      chr_dict[character] = 1
    else:
      chr_dict[character] += 1
  return unique_chr, chr_dict

unique_chr, chr_dict = get_chrdict(word)
max_value = max(chr_dict.values())
ans_list = [i[0] for i in chr_dict.items() if i[1] == max_value]
if len(ans_list) > 1:
  print('?')
else:
  print(ans_list[0].upper())
