class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        pos = set()
        neg = set()

        ret = []
        
        cur = [["." for k in range(n)] for l in range(n)]
        print(cur)

        def dfs(r):
            if r >= n:

                temp = []
                for row in cur:
                    temp.append("".join(row))
                ret.append(temp)
                return

            for i in range(n):
                if i not in col and (r + i) not in pos and (r - i) not in neg:
                    cur[r][i] = "Q"

                    col.add(i)
                    pos.add(r + i)
                    neg.add(r - i)

                    dfs(r + 1)

                    cur[r][i] = "."
                    col.remove(i)
                    pos.remove(r + i)
                    neg.remove(r - i)
        
        dfs(0)
        return ret
