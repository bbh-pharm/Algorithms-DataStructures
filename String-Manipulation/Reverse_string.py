######################
## Two pointer swap ##
######################
def reverse_string(s):
  left, right = 0, len(s) - 1
  while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

a = ['h', 'e', 'l', 'l', 'o']
reverse_string(a)
print(a)

#######################
## Using list method ##
#######################
def reverse_string(s):
  s.reverse()

a = ['h', 'e', 'l', 'l', 'o']
reverse_string(a)
print(a)
