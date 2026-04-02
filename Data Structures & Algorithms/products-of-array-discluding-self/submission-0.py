class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for i in nums]

        count = 1

        for i in range(len(nums)):
            ans[i] *= count
            count *= nums[i]
        
        count = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= count
            count *= nums[i]
        
        return ans