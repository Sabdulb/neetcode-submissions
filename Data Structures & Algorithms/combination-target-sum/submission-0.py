class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ret = []

        subarray = []

        def dfs(i, tot):

            if tot > target:
                return
            elif tot == target:
                ret.append(subarray.copy())
                return

            if i >= len(nums):
                return
            
            subarray.append(nums[i])

            dfs(i, tot + nums[i])

            subarray.pop()

            dfs(i + 1, tot)

        dfs(0, 0)

        return ret
                