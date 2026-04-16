class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        heap = []
        visit = set()

        def dist(x1,y1,x2,y2):

            return abs(x1 - x2) + abs(y1-y2)

        cost = [float("inf")] * len(points)

        heapq.heappush(heap, (0, 0))
        cost[0] = 0

        while heap:

            dists, point = heapq.heappop(heap)

            if point in visit:
                continue
            
            visit.add(point)

            cost[point] = min(cost[point], dists)

            for i in range(len(points)):

                if i in visit:
                    continue
                
                pair = points[i]
                x1 = points[point][0]
                y1 = points[point][1]
                x2 = points[i][0]
                y2 = points[i][1]

                dists = dist(x1,y1,x2,y2)

                heapq.heappush(heap, (dists, i) )
        
        ret = 0

        for val in cost:
            ret += val
        
        return ret