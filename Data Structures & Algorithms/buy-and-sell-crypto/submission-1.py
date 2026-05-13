class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = prices[0]
        ret = 0
        
        for num in prices:
            ret = max(ret, num - l)

            if num < l:
                l = num
        
        return ret