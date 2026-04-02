class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.isWord = True
        

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if c not in root.children:
                return False
            root = root.children[c]
        return root.isWord

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c not in root.children:
                return False
            root = root.children[c]
        return True
        