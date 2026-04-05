class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        visit = set()
        q = deque()

        ROWS,COLS = len(grid), len(grid[0])

        def bfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or ((i,j) in visit) or grid[i][j] != 1:
                return
            
            visit.add((i,j))
            q.append([i,j])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    visit.add((i,j))
                    q.append([i,j])
        
        minute = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                bfs(r + 1,c)
                bfs(r - 1,c)
                bfs(r,c + 1)
                bfs(r,c - 1)
            if not q:
                break
            minute += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in visit:
                    return -1

        return minute