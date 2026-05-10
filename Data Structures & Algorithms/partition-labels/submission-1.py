class Solution:
    def partitionLabels(self, s: str) -> List[int]:
       
        ret = []
        mp = {}
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = [i,i]
            else:
                mp[s[i]][1] = i
        
        vals = list(mp.values())
        temp = vals[0]
        for i in range(1, len(vals)):
            if vals[i][0] <= temp[1]:
                temp[0] = min(temp[0], vals[i][0])
                temp[1] = max(temp[1], vals[i][1])
            else:
                ret.append(temp[1] - temp[0] + 1)
                temp = vals[i]
        
        ret.append(temp[1] - temp[0] + 1)

        return ret