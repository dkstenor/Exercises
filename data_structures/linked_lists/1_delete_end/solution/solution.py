# Write your answers here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self, head = None):
        self.head = head

    def delete_at_end(self):
        if self.head is None:
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None


