#leet code singly linked list





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        # current_node.prev = new_node
        new_node.prev = current_node

    def printing(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


#node <-> new_node 

test = Linkedlist()
test.add_node(1)
test.add_node(2)
test.add_node(3)
test.printing()        
        
            
        
