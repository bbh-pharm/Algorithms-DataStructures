input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagrams(input_list):
  result = {}
  for word in input_list:
    sorted_word = "".join(sorted(word))
    if sorted_word not in result:
      result[sorted_word] = [word]
    else:
      result[sorted_word].append(word)
  return list(result.values())

group_anagrams(input_list)
