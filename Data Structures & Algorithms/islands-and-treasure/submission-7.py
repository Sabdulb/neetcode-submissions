class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        visit = set()
        ROWS,COLS = len(grid), len(grid[0])

        def bfs(i,j):
            if min(i,j) < 0 or i >= ROWS or j >= COLS or (i,j) in visit or grid[i][j] == -1:
                return
            
            visit.add((i,j))
            q.append((i,j))
        
        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 0:
                    visit.add((i,j))
                    q.append((i,j))
        
        dist = 0
        while q:
            for i in range(len(q)):
                i,j = q.popleft()
                grid[i][j] = dist

                bfs(i + 1,j)
                bfs(i - 1,j)
                bfs(i,j + 1)
                bfs(i,j - 1)
            dist += 1
