class Solution:
    def isValid(self, s: str) -> bool:
        
        
        mp = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for c in s:

            if c in mp:

                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if temp != mp[c]:
                    return False
            else:
                stack.append(c)
        
        if len(stack) > 0:
            return False
        else:
            return True


