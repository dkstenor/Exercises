#Write your Answers here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, data):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next

        cur_node.next = Node(data)