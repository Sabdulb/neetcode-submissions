class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        heapq.heapify_max(heap)
        
        for xi,yi in points:
            dist = abs( math.sqrt( math.pow(0 - xi, 2) + math.pow(0 - yi, 2) ) )
            heapq.heappush_max(heap, [dist,xi,yi])

            while len(heap) > k:
                heapq.heappop_max(heap)
        
        ret = []

        for dist,x,y in heap:
            ret.append([x,y])
        
        return ret