class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        dp = {}

        def dfs(i,j):
            if j == len(t):
                dp[(i,j)] = 1
                return 1
            if i >= len(s):
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp[(i,j)] = 0
            if s[i] == t[j]:
                dp[(i,j)] += dfs(i + 1, j + 1)
            dp[(i,j)] += dfs(i + 1, j)
            return dp[(i,j)]
        
        return dfs(0,0)
            


