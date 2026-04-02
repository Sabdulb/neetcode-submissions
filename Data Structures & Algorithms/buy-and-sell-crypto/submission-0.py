class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        l = 0
        r = 0
        while r < len(prices):
            
            ret = max(prices[r] - prices[l], ret)

            if prices[r] < prices[l]:
                l = r

            r += 1


        return ret