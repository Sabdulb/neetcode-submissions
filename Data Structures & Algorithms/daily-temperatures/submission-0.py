class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0 for temp in temperatures]
        stack = []

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(i)
                continue
            
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                temp = stack.pop()
                arr[temp] = i - temp
            
            stack.append(i)
            
        return arr