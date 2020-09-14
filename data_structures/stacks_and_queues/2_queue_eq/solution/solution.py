class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.tail_node:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node
            self.tail_node = new_node

    def dequeue(self):
        if not self.head_node:
            raise IndexError
        value = self.head_node.value
        self.head_node = self.head_node.next
        if not self.head_node:
            self.tail_node = None
        return value

    # You may want to solve this magic method first!
    # def __len__(self):
    #     return

    # Fill in the code for __len__ls

    def __eq__(self, other):
        if (len(self) == len(other)):
            node1 = self.head_node
            node2 = other.head_node
            while(node1):
                if node1.value == node2.value:
                    return False
                else:
                    node1 = node1.next
                    node2 = node2.next
                return True
        return False
