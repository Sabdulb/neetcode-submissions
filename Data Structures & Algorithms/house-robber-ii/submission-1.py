class Solution:
    def rob(self, nums: List[int]) -> int:


        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        rums = nums[::-1]

        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)

        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[0] = rums[0]
        dp2[1] = max(rums[0], rums[1])


        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i-1], nums[i] + dp1[i-2])
            dp2[i] = max(dp2[i-1], rums[i] + dp2[i-2])
        
        print(dp1)
        print(dp2)

        return max(dp1[len(nums) - 2], dp2[len(nums) - 2])