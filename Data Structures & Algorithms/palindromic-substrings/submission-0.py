class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ret = 0

        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j-1]):
                    dp[i][j] = True
                    ret += 1
        
        return ret