class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        arr = [[0 for _ in range(n)] for _ in range(n)]
        mp = defaultdict(set)

        for p,q in edges:
            mp[p].add(q)
            mp[q].add(p) 
            arr[p][q] = 1
            arr[q][p] = 1
        
        def dfs(node, prev, visit):

            if node in visit or node == prev:
                return False
            
            visit.add(node)

            counter = False
            
            for i in range(n):
                if i != prev and arr[node][i] != 0:
                    counter = True
                    if dfs(i, node, visit) == False:
                        return False
            
            return Counter
        
        visit = set()
        if dfs(0, -1, visit) == False:
            return False

        for i in range(n):
            if i not in visit:
                return False

        return True