# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

##############################
## Using recursive function ##
##############################
def reverseList(head):
    def reverse(node, prev):
      if not node:
        return prev
      next, node.next = node.next, prev
      return reverse(next, node)
    return reverse(head)

################
## Using loop ##
################
def reverseList(head):
  node, prev = head, None

  while node:
    next, node.next = node.next, prev
    prev, node = node, next

  return prev
