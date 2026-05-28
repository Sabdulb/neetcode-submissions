class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        mp = {}

        for l,r in intervals:

            for i in range(l, r + 1):
                if i not in mp:
                    mp[i] = r - l + 1
                else:
                    mp[i] = min(r - l + 1, mp[i])
        
        ret = []

        for val in queries:
            ret.append(mp.get(val, -1))
        
        return ret