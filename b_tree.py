class BTreeNode:
    def __init__(self, t):
        self.keys = []
        self.children = []
        self.leaf = True
        self.t = t  # minimum degree

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    # Methods for insertion, deletion, search omitted for brevity
