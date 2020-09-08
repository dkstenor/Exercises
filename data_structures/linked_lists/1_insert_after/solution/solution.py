# Write your answers here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_after_item(self, x, data):
        genesis = self.head
        if self.head == None:
            return
        while self.head.next != None:
            print(self.head.data)
            if self.head.data == x:
                tmp_node = self.head
                self.head.next = Node(data)
                self.head.next.next = tmp_node
                self.head = genesis
                return
            else:
                self.head = self.head.next

items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(50)
items.insert_after_item(30, 0)