class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 3:
            return max(nums[0] + nums[2], nums[1])
        elif n == 2:
            return max(nums[0], nums[1])
        elif n == 1:
            return nums[0]
        
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return max(dp[n-1], dp[n-2])
