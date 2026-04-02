class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        mp = {}
        for s in strs:
            t = sorted(s)
            t = str(t)
            if t in mp:
                mp[t].append(s)
            else:
                mp[t] = []
                mp[t].append(s)
        for key in mp:
            ans.append(mp[key])
        
        return ans
    