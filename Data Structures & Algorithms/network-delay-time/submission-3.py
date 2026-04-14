class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        mp = defaultdict(list)

        heap = []

        visit = set()

        for u,v,t in times:
            mp[u].append((t,v))
        
        heapq.heappush(heap, (0,k))
        ret = 0
        while heap:

            t,n1 = heapq.heappop(heap)

            if n1 in visit:
                continue
            
            visit.add(n1)

            ret = max(ret, t)
            for t2,n2 in mp[n1]:
                heapq.heappush(heap, (t2 + t, n2))
        
        if len(visit) == n:
            return ret
        
        return -1
