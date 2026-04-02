class MedianFinder:

    def __init__(self):
        self.top = []
        self.bottom = []
        heapq.heapify(self.top)
        heapq.heapify_max(self.bottom)

    def addNum(self, num: int) -> None:
        
        if len(self.bottom) == 0 or num >= self.bottom[0]:
            heapq.heappush(self.top, num)
        else:
            heapq.heappush_max(self.bottom, num)

        while len(self.top) < len(self.bottom) or (len(self.top) - len(self.bottom) > 1):
            if len(self.top) < len(self.bottom):
                temp = heapq.heappop_max(self.bottom)
                heapq.heappush(self.top, temp)
            else:
                temp = heapq.heappop(self.top)
                heapq.heappush_max(self.bottom, temp)
        



    def findMedian(self) -> float:
        if len(self.top) > len(self.bottom):
            return self.top[0]
        else:
            return (self.top[0] + self.bottom[0]) / 2