class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        arr = [[0 for _ in range(n)] for _ in range(n)]

        for p,q in edges: 
            arr[p][q] = 1
            arr[q][p] = 1
        
        def dfs(node, prev, visit):

            if node in visit or node == prev:
                return False
            
            visit.add(node)
            
            for i in range(n):
                if i != prev and arr[node][i] != 0:
                    if dfs(i, node, visit) == False:
                        return False
    
            return True
        
        visit = set()
        if dfs(0, -1, visit) == False or len(visit) != n:
            return False

        return True