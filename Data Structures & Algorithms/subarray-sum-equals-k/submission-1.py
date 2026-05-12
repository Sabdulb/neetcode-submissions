class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ret = 0
        sums = 0
        mp = {}
        mp[sums] = 1

        for num in nums:
            sums += num

            if sums - k in mp:
                ret += mp[sums - k]
            
            if sums in mp:
                mp[sums] += 1
            else:
                mp[sums] = 1
        
        return ret