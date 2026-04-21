class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        INF = float("inf")

        dp = [INF] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):

            for c in coins:

                if amount - c >= 0:

                    dp[i] = min(dp[i], 1 + dp[i - c])

        if dp[amount] == INF:
            return -1
        else:
            return dp[amount]

            
