class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ret = False

        def dfs(i,j, cur):

            if board[i][j] != word[cur]:
                return False
            
            if cur >= len(word) - 1:
                return True
            
            ret = False

            temp = board[i][j]
            board[i][j] = "."

            if i < len(board) - 1:
                ret = ret or dfs(i + 1, j, cur + 1)
            if i > 0:
                ret = ret or dfs(i - 1, j, cur + 1)
            if j < len(board[i]) - 1:
                ret = ret or dfs(i, j + 1, cur + 1)
            if j > 0:
                ret = ret or dfs(i, j - 1, cur + 1)

            board[i][j] = temp

            return ret
        
        for i in range(len(board)):
            for j in range(len(board[i])):

                ret = dfs(i,j, 0)

                if ret == True:
                    return ret
            
        return ret


                    

            



