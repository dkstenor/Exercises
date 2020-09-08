# Write your solution here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def delete_item_by_value(self, x):
        cur_node = self.head
        prev_node = cur_node
        while cur_node.data != None and cur_node.data != x:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node.next != None:
            prev_node.next = cur_node.next

items = linkedList()
items.head = Node(20)
items.head.next = Node(30)
items.head.next.next = Node(40)
items.head.next.next.next = Node(50)
items.delete_item_by_value(40)