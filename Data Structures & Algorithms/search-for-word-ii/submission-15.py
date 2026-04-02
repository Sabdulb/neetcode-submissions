class Trie:
    def __init__(self):
        self.children = {}
        self.isword = None
    
    def addWord(self, word):
        temp = self
        for c in word:
            if c in temp.children:
                temp = temp.children[c]
            else:
                temp.children[c] = Trie()
                temp = temp.children[c]
        temp.isword = word
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        ret = set()
        for word in words:
            root.addWord(word)
        
        def dfs(i,j,node):
            if node.isword is not None:
                ret.add(node.isword)
            
            if i < 0 or i > len(board) - 1:
                return
            if j < 0 or j > len(board[i]) - 1:
                return
            if board[i][j] in node.children:
                lett=board[i][j]
                board[i][j] = "#"
                dfs(i + 1, j, node.children[lett])
                dfs(i - 1, j, node.children[lett])
                dfs(i, j + 1, node.children[lett])
                dfs(i, j - 1, node.children[lett])
                board[i][j] = lett
            else:
                return
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i,j,root)
        
        return list(ret)