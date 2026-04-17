class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        heap = []

        dist = [[1,0], [-1,0], [0,1], [0,-1]]

        heapq.heappush(heap, (grid[0][0],0,0))

        visit = set()

        while heap:

            t,r,c = heapq.heappop(heap)

            if r == n-1 and c == n-1:
                return t
            
            for i,j in dist:

                newR, newC = r + i, j + c

                if min(newR,newC) < 0 or max(newR,newC) >= n or (newR,newC) in visit:
                    continue
                
                visit.add((newR, newC))
                heapq.heappush(heap, (max(t, grid[newR][newC]), newR, newC))

