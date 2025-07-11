import random

class Node:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None]*(level+1)

class SkipList:
    def __init__(self, max_level=16):
        self.max_level = max_level
        self.head = Node(None, max_level)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < 0.5 and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, val):
        update = [None]*(self.max_level+1)
        cur = self.head
        for i in reversed(range(self.level+1)):
            while cur.forward[i] and cur.forward[i].val < val:
                cur = cur.forward[i]
            update[i] = cur
        lvl = self.random_level()
        if lvl > self.level:
            for i in range(self.level+1, lvl+1):
                update[i] = self.head
            self.level = lvl
        node = Node(val, lvl)
        for i in range(lvl+1):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node
