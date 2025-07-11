class HashMap:
    def __init__(self):
        self.map = {}

    def put(self, key, val):
        self.map[key] = val

    def get(self, key):
        return self.map.get(key)
