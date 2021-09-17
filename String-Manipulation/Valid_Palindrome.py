#####################
## Using only list ##
#####################
def isPalindrome(s:str) -> bool:
  strs = []
  for char in s:
    if char.isalnum(): # Function of isalnum is to check alphabets and numbers
      strs.append(char.lower())

  # Check palindrome
  while len(strs) > 1:
    if strs.pop(0) != strs.pop():
      return False
  
  return True

print(isPalindrome("a man, a plan, a canal: Panama"))

#####################
##   Using Deque   ##
#####################
from collections import deque

def isPalindrome(s:str) -> bool:
  strs: Deque = deque()

  for char in s:
    if char.isalnum():
      strs.append(char.lower())

  while len(strs) > 1:
    if strs.popleft() != strs.pop():
      return False
  
  return True

print(isPalindrome("a man, a plan, a canal: Panama"))

#####################
##  Using slicing  ##
#####################
import re

def isPalindrome(s: str) -> bool:
  s = s.lower()
  # filtering using re
  s = re.sub('[^a-z0-9]', '', s)

  return s == s[::-1]

print(isPalindrome("a man, a plan, a canal: Panama"))
