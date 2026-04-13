class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges) + 1
        rank = [1] * n
        par = [i for i in range(n)]

        def find(n1):

            ret = n1

            while ret != par[ret]:
                par[ret] = par[par[ret]]
                ret = par[ret]
            
            return ret
        
        def union(n1,n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return False
            
            if rank[r2] > rank[r1]:
                rank[r2] += rank[r1]
                par[r1] = r2
            else:
                rank[r1] += rank[r2]
                par[r2] = r1
            
            return True
        
        for e,v in edges:
            if not union(e,v):
                return [e,v]
        
        return [-1,-1]