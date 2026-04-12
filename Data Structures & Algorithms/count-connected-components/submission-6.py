class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        par = [i for i in range(n)]

        rank = [1] * n

        def find(n1):

            ret = n1

            while ret != par[ret]:
                par[ret] = par[par[ret]]
                ret = par[ret]
            
            return ret
        
        def union(n1, n2):

            r1,r2 = find(n1), find(n2)

            if r1 == r2:
                return 0
            
            if rank[r2] > rank[r1]:
                par[r1] = par[r2]
                rank[r2] += rank[r1]
            else:
                par[r2] = par[r1]
                rank[r1] += rank[r2]
            
            return 1
        
        ans = n
        for n1, n2 in edges:
            ans -= union(n1,n2)
        return ans