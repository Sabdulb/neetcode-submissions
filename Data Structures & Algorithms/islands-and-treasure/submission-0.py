class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        
        def dfs(i, j):

            if i >= ROWS or i < 0 or j >= COLS or j < 0 or (i,j) in visited:
                return -1000000
            
            if grid[i][j] == 0:
                return 1
            
            visited.add((i,j))

            p1 = dfs(i,j)
            p1 = dfs(i,j)
            p1 = dfs(i,j)
