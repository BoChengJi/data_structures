class BloomFilterSimple:
    def __init__(self, size):
        self.size = size
        self.bit_array = [0]*size

    def add(self, item):
        idx = hash(item) % self.size
        self.bit_array[idx] = 1

    def check(self, item):
        idx = hash(item) % self.size
        return self.bit_array[idx] == 1
