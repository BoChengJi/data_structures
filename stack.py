class Stack:
    def __init__(self):
        self.data = []
    def push(self, val):
        self.data.append(val)
    def pop(self):
        if self.data:
            return self.data.pop()
        return None
