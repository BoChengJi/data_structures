class KDNode:
    def __init__(self, point, axis=0):
        self.point = point
        self.left = None
        self.right = None
        self.axis = axis

class KDTree:
    def __init__(self):
        self.root = None
