# Aadil Rashid Reverse linked list 9.29.24
# 
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # will become the new head to reverse
        current = head #start of the head of the initial list 

        while current:
            next_node = current.next #saving the next node
            current.next = prev #reverse the pointer
            prev = current #moving prev to current node
            current = next_node #moviing to next node in the original list

        return prev #prv is now the new head of the reversed list
    
   