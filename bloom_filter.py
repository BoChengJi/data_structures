import hashlib

class BloomFilter:
    def __init__(self, size=1000):
        self.size = size
        self.bit_array = [0] * size

    def _hashes(self, item):
        return [hash(item) % self.size, int(hashlib.md5(item.encode()).hexdigest(), 16) % self.size]

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def check(self, item):
        return all(self.bit_array[h] for h in self._hashes(item))
