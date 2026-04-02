class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arr = [[position[i], speed[i]] for i in range(len(position))]

        stack = []

        for p,s in sorted(arr)[::-1]:
            stack.append((target - p) / s)

            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()

                if a <= b:
                    stack.append(b)
                else:
                    stack.append(b)
                    stack.append(a)
        
        return len(stack)
