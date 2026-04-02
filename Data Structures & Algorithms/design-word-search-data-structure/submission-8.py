class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.isWord = True

    def search(self, word: str) -> bool:
        
        def dfs(i, node):

            if i >= len(word):
                return node.isWord

            ret = False
            
            if word[i] == ".":
                for c in node.children.keys():
                    ret = ret | dfs(i + 1, node.children[c])
                    if ret:
                        return True
            else:
                if word[i] not in node.children:
                    return False
                else:
                    return dfs(i + 1, node.children[word[i]])
            
            return False

        return dfs(0, self.root)
