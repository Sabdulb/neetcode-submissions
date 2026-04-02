class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.root

        for c in word:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        
        temp.isWord = True

    def search(self, word: str) -> bool:

        temp = self.root

        def dfs(i, node):

            ret = False

            if i >= len(word):
                return node.isWord
            
            if word[i] == ".":
                for c in node.children.keys():
                    ret = ret | dfs(i + 1, node.children[c])

            else:
                if word[i] not in node.children:
                    return False
                else:
                    ret = ret | dfs(i + 1, node.children[word[i]])
            
            return ret
        
        return dfs(0, temp)
        
