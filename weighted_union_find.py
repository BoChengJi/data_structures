class WeightedUnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.weight = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            orig = self.parent[x]
            self.parent[x] = self.find(orig)
            self.weight[x] += self.weight[orig]
        return self.parent[x]

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.parent[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
