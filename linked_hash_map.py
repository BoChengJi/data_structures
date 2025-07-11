class LinkedHashMap:
    def __init__(self):
        self.map = {}
        self.order = []

    def put(self, key, val):
        if key not in self.map:
            self.order.append(key)
        self.map[key] = val

    def get(self, key):
        return self.map.get(key)

    def keys(self):
        return self.order
