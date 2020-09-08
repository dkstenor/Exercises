# Write your answers here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_start(self, data):
        genesis = self.head
        self.head = Node(data)
        self.head.next = genesis
 

items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(50)
items.insert_at_start(12)
print(items.head.data)
