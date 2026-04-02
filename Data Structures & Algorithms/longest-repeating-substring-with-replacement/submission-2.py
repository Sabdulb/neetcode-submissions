class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        top = 0
        t = ""
        ret = 0
        l = 0
        mp = {}

        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1

            if mp[s[r]] > top:
                t = s[r]
                top = mp[s[r]]

            while (r - l + 1) > top + k:
                mp[s[l]] -= 1
                l += 1

            ret = max(ret, r - l + 1)
            print(f'{l} {r} {ret} {s[l:r]} {top + k}')

        return ret

            



            
