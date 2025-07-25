import mmh3
from bitarray import bitarray

class BloomFilterAdvanced:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = True

    def check(self, item):
        return all(self.bit_array[mmh3.hash(item, i) % self.size] for i in range(self.hash_count))
