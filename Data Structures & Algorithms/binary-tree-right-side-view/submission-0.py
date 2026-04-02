# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        mp = {}
        ans = []

        def dive(node, level):

            if node == None:
                return
            
            if level not in mp:
                mp[level] = []
            mp[level].append(node.val)
            dive(node.right, level + 1)
            dive(node.left, level + 1)
        
        dive(root, 0)

        for key in mp.keys():
            ans.append(mp[key][0])
        
        return ans