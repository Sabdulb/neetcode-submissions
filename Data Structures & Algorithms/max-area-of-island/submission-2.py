class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ret = [0]
        sub = [0]

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(i, j):
            
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0:
                return
            else:
                sub[0] += 1
                ret[0] = max(ret[0], sub[0])
                grid[i][j] = 0
                dfs(i + 1,j)
                dfs(i - 1,j)
                dfs(i,j + 1)
                dfs(i,j - 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                sub = [0]
                dfs(i, j)
        
        return ret[0]
            
