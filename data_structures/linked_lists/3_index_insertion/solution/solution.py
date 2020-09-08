#Write your answers here 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_index(self, index, data):
        new_node = Node(data)
        idx = 1
        cur_node = self.head
        prv_node = cur_node
        while idx < index:
            prv_node = cur_node
            cur_node = cur_node.next
            idx += 1
        prv_node.next = new_node
        new_node.next = cur_node
        

items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)
items.insert_at_index(2, 2)
print(items.head.data)
print(items.head.next.data)
print(items.head.next.next.data)
print(items.head.next.next.next.data)
