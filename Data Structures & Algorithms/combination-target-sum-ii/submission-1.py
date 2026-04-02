class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []

        candidates.sort()
        
        def dfs(i, arr, tot):

            if tot == target:
                ret.append(arr.copy())
                return
            
            if tot > target or i >= len(candidates):
                return
            
            arr.append(candidates[i])

            dfs(i + 1, arr, tot + candidates[i])

            arr.pop()

            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, arr, tot)

        
        dfs(0, [], 0)

        return ret