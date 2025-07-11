class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)
