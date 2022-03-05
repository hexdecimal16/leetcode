# https://leetcode.com/problems/merge-nodes-in-between-zeros/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # in -> [0,3,1,0,4,5,2,0]
    # out -> [4,11]
    p = head
    while head.next != None:
      sum = head.val
      crrhead = head
      if head.val == 0:
        head = head.next
        while head.val != 0:
          sum += head.val
          head = head.next
      else:
        head = head.next
      newNode = ListNode(sum)
      crrhead.next = newNode
      # newNode.next = head
    ptr = p
    while ptr.next != None:
      nxt = ptr.next
      print(f"next. {nxt.val}, {nxt.next}\n")
      if nxt.val == 0:
        print(f"skipping {nxt.val}, nodes: {nxt.next} \n")
        ptr = nxt.next
      ptr = ptr.next

      
    return p.next


