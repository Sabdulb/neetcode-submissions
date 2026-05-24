class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0 or len(intervals) == 1:
            return 0
        
        intervals.sort(key=lambda pair: pair[0])

        temp = intervals[0]
        ret = 0

        for i in range(1, len(intervals)):
            if temp[1] <= intervals[i][0]:
                temp = intervals[i]
            else:
                ret += 1
                temp[1] = min(temp[1],intervals[i][1])
        
        return ret