class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}

        def dfs(i,buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i,buying)]
            
            dp[(i,buying)] = 0
            if buying:
                dp[(i,buying)] = max(dfs(i + 1, buying), dfs(i + 1, not buying) - prices[i])
            if not buying:
                dp[(i,buying)] = max(dfs(i + 1, buying), prices[i] + dfs(i + 2, not buying))
            return dp[(i,buying)]
        
        return dfs(0, True)