class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ret = []

        l,r = newInterval[0], newInterval[1]

        for i,j in intervals:

            if (l >= i and l <= j) or (l <= i and r >= i) or (l <= j and r >= j):
                l,r = min(i,l), max(j,r)
            elif i < l:
                ret.append([i,j])
            else:
                ret.append([l,r])
                l,r = i,j
        
        ret.append([l,r])
        return ret