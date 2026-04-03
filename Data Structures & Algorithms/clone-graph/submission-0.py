"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        mp = {}

        visited = set()

        def build(edge):

            if not edge or edge.val in visited:
                return
            
            visited.add(edge.val)

            mp[edge.val] = Node(edge.val)

            for n in edge.neighbors:
                build(n)
        
        def neighbor(edge):

            if not edge or edge.val in visited:
                return
            
            visited.add(edge.val)

            mp[edge.val].neighbors = []

            for n in edge.neighbors:
                mp[edge.val].neighbors.append(mp[n.val])
                neighbor(n)
            
        build(node)
        visited = set()
        neighbor(node)

        return mp.get(1, None)
            
                
        

