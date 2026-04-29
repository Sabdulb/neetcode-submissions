class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}

        def dfs(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i + 1, j + 1)
            else:
                # (i + 1, j) is deleting as you check the same letter in string 2 but against the next string 1 char
                # (i, j + 1) is inserting as you mark j as complete since you "inserted" and then check the next string 2 char against the current string 1 char
                # (i + 1, j + 1) is replacing as you just proceed as normal
                dp[(i,j)] = min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
                dp[(i,j)] += 1
            
            return dp[(i,j)]
        
        return dfs(0, 0)
                

