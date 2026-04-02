class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        ret = 0
        mp = set()

        while r < len(s):
            
            print(mp)

            if s[r] not in mp:
                mp.add(s[r])
            else:
                while s[r] in mp:
                    mp.remove(s[l])
                    l += 1
                mp.add(s[r])

            r += 1

            ret = max(ret, r - l)
    
        return ret