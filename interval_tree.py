class IntervalNode:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval[1]
        self.left = None
        self.right = None

class IntervalTree:
    def __init__(self):
        self.root = None

    # Insertion and other methods omitted for brevity
