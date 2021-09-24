# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

####################
## Change to list ##
####################
def isPalindrome(head):
    q = []
        
    if not head:
        return True
    node = head
    # Change to list
    while node is not None:
        q.append(node.val)
        node = node.next
    # Determine palindrome
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True

#################
## Using deque ##
#################
from collections import deque

def isPalindrome(head):
    q = deque()
        
    if not head:
        return True
    node = head
    # Change to list
    while node is not None:
        q.append(node.val)
        node = node.next
    # Determine palindrome
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True

##################
## Using runner ##
##################
# I need to understand this problem more...
def isPalindrome(head):
  rev = None
  slow = fast = head

  while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next
  if fast:
    slow = slow.next
  
  while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next

  return not rev
