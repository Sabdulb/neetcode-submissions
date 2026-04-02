class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = None
    
    def addWord(self, s):
        temp = self
        for c in s:
            if c not in temp.children:
                temp.children[c] = TrieNode()
            temp = temp.children[c]
        temp.isWord = s
                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ROWS = len(board)
        COLS = len(board[0])

        ret = set()

        root = TrieNode()

        for word in words:
            root.addWord(word)
        

        def dfs(i,j, path):
            

            if path.isWord:
                ret.add(path.isWord)
            
            if len(path.children) <= 0:
                return

            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            
            if board[i][j] not in path.children:
                return
            
            saved = board[i][j]
            board[i][j] = "."

            dfs(i + 1, j, path.children[saved])
            dfs(i - 1, j, path.children[saved])
            dfs(i, j + 1, path.children[saved])
            dfs(i, j - 1, path.children[saved])

            board[i][j] = saved
        
        for i in range(len(board)):
            for j in range(len(board[i])):

                dfs(i, j, root)
        
        return list(ret)
        
        