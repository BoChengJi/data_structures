import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None

class Treap:
    def __init__(self):
        self.root = None
