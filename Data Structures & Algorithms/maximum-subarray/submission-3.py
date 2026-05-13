class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ret = nums[0]
        cur = 0

        for i,val in enumerate(nums):

            cur = max(cur + val, val)
            ret = max(ret, cur)
        
        return ret