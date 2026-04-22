class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        half = sum(nums) // 2
        dp = [False] * (half + 1)
        dp[0] = True

        for num in nums:
            if num > half:
                return False
            for i in range(len(dp) - 1, -1, -1):
                if i - num >= 0:
                    dp[i] = dp[i] | dp[i-num]
        print(dp)
        return dp[half]