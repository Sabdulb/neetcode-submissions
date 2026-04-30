class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {}

        def dfs(i,a):
            if a == 0:
                return 1
            if i >= len(coins):
                return 0
            
            if (i,a) in dp:
                return dp[(i,a)]
            
            dp[(i,a)] = 0
            if a - coins[i] >= 0:
                dp[(i,a)] = dfs(i + 1, a)
                dp[(i,a)] += dfs(i, a - coins[i])
                
            
            return dp[(i,a)]
        
        return dfs(0,amount)