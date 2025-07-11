class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0]*(2*self.n)
        for i in range(self.n):
            self.tree[self.n+i] = data[i]
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]

    def update(self, pos, val):
        pos += self.n
        self.tree[pos] = val
        while pos > 1:
            pos >>= 1
            self.tree[pos] = self.tree[pos<<1] + self.tree[pos<<1|1]

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res
