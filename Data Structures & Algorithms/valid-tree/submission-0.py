class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        arr = [[0 for _ in range(n)] for _ in range(n)]

        for p,q in edges:
            arr[p][q] = 1
            arr[q][p] = 1
        
        def dfs(node, prev, visit):

            if node in visit:
                return False
            
            visit.add(node)

            counter = False
            
            print(node)
            print(arr[node])
            for i in range(n):
                if i != prev and arr[node][i] != 0:
                    counter = True
                    if dfs(i, node, visit) == False:
                        return False
            
            return Counter
        
        for i in range(n):
            if dfs(i, i, set()) == False:
                return False

        return True