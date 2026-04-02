class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq.heapify_max(stones)
        p = None
        q = None
        if len(stones) > 0:
            p = heapq.heappop_max(stones)
        if len(stones) > 0:
            q = heapq.heappop_max(stones)

        while q:
            if p == q:
                p = None
                q = None
                if len(stones) > 0:
                    p = heapq.heappop_max(stones)
                if len(stones) > 0:
                    q = heapq.heappop_max(stones)
            else:
                diff = abs(p - q)
                heapq.heappush_max(stones, diff)
                p = None
                q = None
                if len(stones) > 0:
                    p = heapq.heappop_max(stones)
                if len(stones) > 0:
                    q = heapq.heappop_max(stones)
        
        if p is None:
            return 0
        else:
            return p
            