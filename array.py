class Array:
    def __init__(self):
        self.data = []
    def append(self, val):
        self.data.append(val)
    def get(self, i):
        return self.data[i]
