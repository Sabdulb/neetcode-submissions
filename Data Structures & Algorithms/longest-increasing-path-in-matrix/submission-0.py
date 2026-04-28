class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp = {}

        def dfs(i,j,prev):
            if min(i,j) < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            dp[(i,j)] = 1 + max( dfs(i+1,j,matrix[i][j]), dfs(i-1,j,matrix[i][j]), dfs(i,j+1,matrix[i][j]), dfs(i,j-1,matrix[i][j]) )
            return dp[(i,j)]
        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                ret = max(ret, dfs(i,j,matrix[i][j] - 1))
        
        return ret