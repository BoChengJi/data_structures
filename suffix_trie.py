class SuffixTrieNode:
    def __init__(self):
        self.children = {}

class SuffixTrie:
    def __init__(self):
        self.root = SuffixTrieNode()

    def insert(self, s):
        for i in range(len(s)):
            node = self.root
            for ch in s[i:]:
                if ch not in node.children:
                    node.children[ch] = SuffixTrieNode()
                node = node.children[ch]
