class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root

        for c in word:
            temp.children[c] = temp.children.get(c, TrieNode())
            temp = temp.children[c]

        temp.isWord = True

    def search(self, word: str) -> bool:
        temp = self.root

        for c in word:
            temp = temp.children.get(c, TrieNode())
        
        return temp.isWord

            
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root

        for c in prefix:
            temp = temp.children.get(c, False)
            if temp is False:
                return temp
        
        return True
        
        