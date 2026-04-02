class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = [0 for h in height]
        right = [0 for p in height]
        lmax = 0
        rmax = 0
        ans = 0

        for i in range(len(height)):
            lmax = max(height[i], lmax)
            left[i] = lmax
        
        for i in range(len(height)-1, -1, -1):
            rmax = max(height[i], rmax)
            right[i] = rmax
        
        for i in range(len(height)):
            ans += abs(min(left[i],right[i]) - height[i]) 
        
        return ans
