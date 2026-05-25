class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        
        ret = 0

        l,r = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):

            if intervals[i][0] >= r:
                l = intervals[i][0]
                r = intervals[i][1]
            else:
                r = min(r, intervals[i][1])
                ret += 1
        
        return ret