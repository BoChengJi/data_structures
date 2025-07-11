class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [None]*k
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, val):
        if self.count == self.size:
            return False
        self.queue[self.tail] = val
        self.tail = (self.tail + 1) % self.size
        self.count += 1
        return True

    def dequeue(self):
        if self.count == 0:
            return None
        val = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return val
