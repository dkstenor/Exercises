# Write your solution here 
#Write your Answers here
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def search(self, x):
        cur_node = self.head
        while cur_node.next != None:
            if cur_node.data == x:
                return True
            cur_node = cur_node.next
        return False
