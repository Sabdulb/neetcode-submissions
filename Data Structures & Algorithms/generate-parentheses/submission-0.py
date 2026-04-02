class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ret = []

        def dfs(cur, opn, cls):
            
            print(cur)
            print(opn)
            print(cls)

            if len(opn) == 0 and len(cls) == 0:
                ret.append(cur)
                return
            
            if opn:

                opn.pop()

                cls.append(1)

                cur += "("

                dfs(cur, opn.copy(), cls.copy())
                
                cur = cur[0:len(cur) - 1]

                opn.append(1)

                cls.pop()
            
            if cls:

                cls.pop()

                cur += ")"

                dfs(cur, opn.copy(), cls.copy())
            
        dfs("", [1 for i in range(n)], [])

        return ret

