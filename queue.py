class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self, val):
        self.data.append(val)
    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None
