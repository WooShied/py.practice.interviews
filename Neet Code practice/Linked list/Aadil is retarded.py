#linked list 
#Definition for singly linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

head = None


def insert(input):
  global head
  node = ListNode(input)
   
  if head is None:
    head =  node
  else: 
    last = head
    while last.next:
      last = last.next

    last.next = node
    

  


def print_list():
    node = head
    while node:
      print(node.val)
      node = node.next


insert (1)
insert (2)
print_list()  

    
   










#create opject node
#check if head is empty or not
#if empty set to new objext
#if its not empty add it to next
#look where you start with head to end till next is empty