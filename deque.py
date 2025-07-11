class Deque:
    def __init__(self):
        self.data = []

    def append(self, val):
        self.data.append(val)

    def appendleft(self, val):
        self.data.insert(0, val)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None

    def popleft(self):
        if self.data:
            return self.data.pop(0)
        return None
