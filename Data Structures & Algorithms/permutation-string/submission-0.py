class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        c1 = Counter(s1)
        mp = {}

        l = 0

        for r in range(len(s2)):
            if s2[r] in c1:
                mp[s2[r]] = mp.get(s2[r],0) + 1

                while mp[s2[r]] > c1[s2[r]]:
                    mp[s2[l]] -= 1
                    l += 1

                if c1 == mp:
                    return True

            else:
                l = r + 1
                mp = {}

        return False

