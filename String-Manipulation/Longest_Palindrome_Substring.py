###############################
## Expansion of two pointers ##
###############################

s = 'babad'

def longest_palindrome(text):
  def expand(left, right, text):
    while left >= 0 and right <= len(text) and text[left] == text[right - 1]:
      left -= 1
      right += 1
    return text[left+1: right-1]

  if len(text) < 2 or text == text[::-1]:
    return text

  result = ''

  for i in range(len(text) - 1):
    result = max(result, expand(i, i + 1, text), expand(i, i + 2, text), key=len)
  return result

print(longest_palindrome(s))
