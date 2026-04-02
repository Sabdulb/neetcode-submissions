class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ret = []

        def dfs(i, cur):
            if i >= len(s):
                ret.append(cur.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j + 1]):

                    cur.append(s[i:j + 1])
                    dfs(j + 1, cur)
                    cur.pop()
        
        dfs(0, [])

        return ret
    
    def isPalindrome(self, s: str):

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True