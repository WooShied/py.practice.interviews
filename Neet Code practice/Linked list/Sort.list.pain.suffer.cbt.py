#Aadil Rashid 9,28.24
#Sort list 

from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next



class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #inital case only 1 node so you only return head
        if not head or not head.next:
            return head
        
        mid = self.getmiddle(head)
        left = head
        right = mid.next
        mid.next = None #breaks list in 2 parts

        #sorting 2 halfs
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        return self.mergeTwoLists(left_sorted, right_sorted)
    
    def getmiddle(self, head: ListNode) -> ListNode:
        #using fast and slow to get middle (yes I used google here to find out how to get to the middle)
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #merge two sorted linked lists
        merged_head = ListNode()
        tail = merged_head

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        #remaining nodes
        if l1:
            tail.next = l1
        else: 
            tail.next = l2

        return merged_head.next #trimps unnessicary placeholders 
