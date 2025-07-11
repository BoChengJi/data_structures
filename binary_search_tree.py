class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = BSTNode(val)
            return
        cur = self.root
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = BSTNode(val)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = BSTNode(val)
                    return
