class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)

        minarr = [1] * n
        maxarr = [1] * n
        minarr[0], maxarr[0] = nums[0], nums[0]
        ret = nums[0]

        for i in range(1, n):
            minarr[i] = min(nums[i], nums[i] * minarr[i-1], nums[i] * maxarr[i-1])
            maxarr[i] = max(nums[i], nums[i] * minarr[i-1], nums[i] * maxarr[i-1])
            ret = max(ret, maxarr[i])
        
        return ret