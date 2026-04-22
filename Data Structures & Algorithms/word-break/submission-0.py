class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = {}
        for i in range(len(wordDict)):
            dp[i] = False
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                print(s[i:i + len(word)])
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    print(i)
                    print(i + len(word))
                    dp[i] = dp.get(i + len(word), False)
                if dp.get(i) == True:
                    break
        
        return dp[0]
            
