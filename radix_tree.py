class RadixNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class RadixTree:
    def __init__(self):
        self.root = RadixNode()

    def insert(self, word):
        node = self.root
        while word:
            for k in node.children:
                common_prefix_len = 0
                while (common_prefix_len < len(k) and common_prefix_len < len(word) and k[common_prefix_len] == word[common_prefix_len]):
                    common_prefix_len += 1
                if common_prefix_len > 0:
                    if common_prefix_len == len(k):
                        node = node.children[k]
                        word = word[common_prefix_len:]
                    else:
                        # split edge
                        old_child = node.children[k]
                        new_child = RadixNode()
                        new_child.children[k[common_prefix_len:]] = old_child
                        node.children[word[:common_prefix_len]] = new_child
                        del node.children[k]
                        node = new_child
                        word = word[common_prefix_len:]
                    break
            else:
                node.children[word] = RadixNode()
                node.children[word].is_end = True
                break
