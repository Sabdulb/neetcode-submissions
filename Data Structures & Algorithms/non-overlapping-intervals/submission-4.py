class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        r = intervals[0][1]
        ret = 0

        for i in range(1, len(intervals)):

            if intervals[i][0] >= r:
                r = intervals[i][1]
                continue
            else:
                ret += 1
                r = min(r, intervals[i][1])
        
        return ret