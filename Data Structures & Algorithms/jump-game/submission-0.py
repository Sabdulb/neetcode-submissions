class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        jump = 0
        for i in range(len(nums)):
            jump = max(jump - 1, nums[i])

            if i < len(nums) - 1 and jump == 0:
                return False
        
        return True