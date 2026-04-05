class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def bfs(i,j):

            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i,j) in visited or grid[i][j] == -1:
                return
            
            visited.add((i,j))
            q.append([i,j])


        dist = 0
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 0:
                    
                    visited.add((i,j))
                    q.append([i,j])
        
        while q:
            for i in range(len(q)):
                [i,j] = q.popleft()
                grid[i][j] = dist

                bfs(i + 1,j)
                bfs(i - 1,j)
                bfs(i,j + 1)
                bfs(i,j - 1)
            dist += 1



