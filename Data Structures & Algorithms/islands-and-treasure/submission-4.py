class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])


        def dfs(i,j,count):
            
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            
            if grid[i][j] <= count:
                return
            
            grid[i][j] = count

            dfs(i + 1,j, count+1)
            dfs(i - 1,j, count+1)
            dfs(i,j + 1, count+1)
            dfs(i,j - 1, count+1)

            return


        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 0:

                    dfs(i + 1,j,1)
                    dfs(i - 1,j,1)
                    dfs(i,j + 1,1)
                    dfs(i,j - 1,1)
        


