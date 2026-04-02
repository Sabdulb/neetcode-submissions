class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)

        ret = 0

        for val in arr:
            count = 0

            if (val - 1) not in arr:
                temp = val
                count += 1
                while (temp + 1) in arr:
                    count += 1
                    temp = temp + 1
            
            ret = max(count,ret)
        
        return ret