##############################
## Using list comprehension ##
##############################

import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']

def common_word(paragraph, banned):
  counts_dicts = {}
  for word in [w.lower() for w in re.sub("[^\w]", " ", paragraph).split() if w not in banned]:
    if counts_dicts.get(word) is None:
      counts_dicts[word] = 1
    else:
      counts_dicts[word] += 1
  ans = {n:w for w, n in counts_dicts.items()}[max(counts_dicts.values())]
  return ans

common_word(paragraph, banned)
