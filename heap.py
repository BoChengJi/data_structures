class Heap:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)
        self._heapify_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            return None
        self._swap(0, len(self.data) - 1)
        val = self.data.pop()
        self._heapify_down(0)
        return val

    def _heapify_up(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.data[idx] < self.data[parent]:
            self._swap(idx, parent)
            self._heapify_up(parent)

    def _heapify_down(self, idx):
        left = idx*2 + 1
        right = idx*2 + 2
        smallest = idx
        if left < len(self.data) and self.data[left] < self.data[smallest]:
            smallest = left
        if right < len(self.data) and self.data[right] < self.data[smallest]:
            smallest = right
        if smallest != idx:
            self._swap(idx, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
