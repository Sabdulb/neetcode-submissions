class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        start = False
        ret = 0
        
        mp = ('+', '-', '*', '/')

        for val in tokens:
            print(stack)
            if val not in mp:
                stack.append(val)
            else:
                temp = 0
                if val == '+':
                    t1 = int(stack.pop())
                    t2 = int(stack.pop())
                    temp = t1 + t2
                elif val == '-':
                    t1 = int(stack.pop())
                    t2 = int(stack.pop())
                    temp = t2 - t1
                elif val == '*':
                    t1 = int(stack.pop())
                    t2 = int(stack.pop())
                    temp = t1 * t2
                elif val == '/':
                    t1 = float(stack.pop())
                    t2 = float(stack.pop())
                    temp = int(t2 / t1)
                stack.append(str(temp))
        return int(stack.pop())
