#Aadil Rashid 9.28.24
#mergind 2 lists 

# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        placeholder = ListNode(0)
        current = placeholder

        # While there are nodes in both lists
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        elif l2:
            current.next = l2  
        
        return placeholder.next      
