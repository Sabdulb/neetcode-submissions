class Solution:
    def jump(self, nums: List[int]) -> int:
        
        ret = 0

        jump = nums[0]

        i = 0

        while i < len(nums) - 1:

            for j in range(i + 1, jump + 1):
                if j >= len(nums) - 1:
                    return ret + 1
                jump = max(jump, j + nums[j])
            
            ret += 1

        return ret