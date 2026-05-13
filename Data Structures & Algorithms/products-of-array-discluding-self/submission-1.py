class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ret = [1] * len(nums)

        cur = 1
        for i in range(len(nums)):
            ret[i] *= cur
            cur *= nums[i]
        
        cur = 1
        for i in range(len(nums)- 1, -1, -1):
            ret[i] *= cur
            cur *= nums[i]
        
        return ret