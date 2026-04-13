class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        nodes = set()
        adj = defaultdict(set)

        for i,j in edges:
            nodes.add(i)
            nodes.add(j)
            adj[i].add(j)
            adj[j].add(i)
        
        def dfs(i, prev, visit):

            if i in visit:
                return False
            
            visit.add(i)

            for val in adj[i]:

                if val != prev:
                    if dfs(val, i, visit) == False:
                        return False
            
            return True
        
        for i,j in edges[::-1]:
            adj[i].remove(j)
            adj[j].remove(i)

            visit = set()
            if dfs(i, i, visit) and len(visit) == len(nodes):
                return [i,j]
            adj[i].add(j)
            adj[j].add(i)
        
        return [-1,-1]