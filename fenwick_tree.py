class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)

    def update(self, i, delta):
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
