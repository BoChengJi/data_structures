class RopeNode:
    def __init__(self, s):
        self.left = None
        self.right = None
        self.s = s
        self.weight = len(s)

class Rope:
    def __init__(self, s):
        self.root = RopeNode(s)
