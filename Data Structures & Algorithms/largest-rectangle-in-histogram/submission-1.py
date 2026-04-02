class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []

        area = 0

        for i,v in enumerate(heights):
            index = i
            height = v

            while stack and stack[-1][1] > v:
                old = stack.pop()
                oldindex = old[0]
                oldheight = old[1]
                area = max(area, oldheight * (i - oldindex))
                index = oldindex
            stack.append([index, height])
    
        for val in stack:
            area = max(area, val[1] * (len(heights) - val[0]))
            
        
        return area

