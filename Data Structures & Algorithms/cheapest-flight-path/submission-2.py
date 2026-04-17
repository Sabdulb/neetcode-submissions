class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        ret = 1000 * 100 + 1

        heap = []

        INF = float("INF")
        adj = [[INF for _ in range(n)] for _ in range(n)]

        for s,d,p in flights:
            adj[s][d] = p
        
        heapq.heappush(heap, (0,0,src))

        while heap:

            cost, steps, cur = heapq.heappop(heap)

            if cur == dst:
                if steps - 1 > k:
                    continue
                return cost
            
            if steps - 1 > k or cost > ret:
                continue
            
            for i in range(len(adj[cur])):

                if i != cur and adj[cur][i] != INF:
                    heapq.heappush(heap, (cost + adj[cur][i], steps + 1, i))
        
        return -1


