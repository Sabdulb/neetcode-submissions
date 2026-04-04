class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        
        def dfs(i, j):
            print(i,j)
            if i >= ROWS or i < 0 or j >= COLS or j < 0 or ((i,j) in visited) or (grid[i][j] == -1):
                return -3147483647
            
            if grid[i][j] == 0:
                return 1
            
            visited.add((i,j))

            p1 = dfs(i+1,j)
            p2 = dfs(i-1,j)
            p3 = dfs(i,j+1)
            p4 = dfs(i,j-1)

            if p1 < 0:
                p1 = 2147483647
            
            if p2 < 0:
                p2 = 2147483647
            
            if p3 < 0:
                p3 = 2147483647
            
            if p4 < 0:
                p4 = 2147483647
            
            grid[i][j] = min(grid[i][j], p1, p2, p3, p4)

            visited.remove((i,j))

            return 1 + grid[i][j]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2147483647:
                    dfs(i,j)

