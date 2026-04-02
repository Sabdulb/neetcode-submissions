class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        q = deque()

        count = Counter(tasks)

        arr = [cnt for cnt in count.values()]

        heapq.heapify_max(arr)

        t = 0

        while arr or q:
            t += 1

            if arr:
                temp = heapq.heappop_max(arr)
                if temp - 1 > 0:
                    q.append([temp - 1, t + n])
            
            if q and q[0][1] == t:
                temp = q.popleft()
                if temp[0] > 0:
                    heapq.heappush_max(arr, temp[0])
            print(t)
            print(q)
        
        return t

