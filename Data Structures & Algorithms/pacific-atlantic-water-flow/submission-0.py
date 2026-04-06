class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        atlantic =  set()
        pacific = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(i, j, prev, ocean):

            if ocean == "atlantic":
                ret = atlantic
            else:
                ret = pacific

            if i < 0 or i >= ROWS or j < 0 or j >= COLS or heights[i][j] < prev or (i,j) in ret:
                return
            else:
                ret.add((i,j))

                dfs(i + 1,j,heights[i][j], ocean)
                dfs(i - 1,j,heights[i][j], ocean)
                dfs(i,j + 1,heights[i][j], ocean)
                dfs(i,j - 1,heights[i][j], ocean)


        for i in range(ROWS):
            for j in range(COLS):

                if i == 0 or j == 0:
                    dfs(i, j, heights[i][j], "pacific")
                
                if i == ROWS - 1 or j == COLS - 1:
                    dfs(i, j, heights[i][j], "atlantic")
        print(pacific)
        print(atlantic)
        ans = []
        for i in range(ROWS):
            for j in range(COLS):

                if (i,j) in atlantic and (i,j) in pacific:
                    ans.append([i,j])
        
        return ans