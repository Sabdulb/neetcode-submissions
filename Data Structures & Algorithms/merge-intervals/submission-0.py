class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        ret = []

        l,r = intervals[0]

        for i in range(1, len(intervals)):
            
            x,y = intervals[i][0], intervals[i][1]

            if x > r:
                ret.append([l,r])
                l,r = x,y
            elif l > y:
                ret.append([x,y])
            else:
                l = min(l,x)
                r = max(r,y)
        
        ret.append([l,r])
        return ret