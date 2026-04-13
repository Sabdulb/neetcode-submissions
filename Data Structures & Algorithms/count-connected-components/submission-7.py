class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rank = [1] * n
        ret = n

        def find(n1):
            
            ret = n1
            while ret != par[ret]:
                ret = par[par[ret]]
                par[ret] = par[ret]
            
            return ret
        
        def union(n1, n2):

            r1,r2 = find(n1), find(n2)

            if r1 == r2:
                return 0

            if rank[r2] > rank[r1]:
                rank[r2] += rank[r1]
                par[r1] = r2
                return 1
            else:
                rank[r1] += rank[r2]
                par[r2] = r1
                return 1
        
        for i,j in edges:
            ret -= union(i,j)
        
        return ret
