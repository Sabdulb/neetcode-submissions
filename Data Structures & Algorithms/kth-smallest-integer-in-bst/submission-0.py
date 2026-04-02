# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr = []

        def dive(node):
            if node is None:
                return
            
            dive(node.left)
            arr.append(node.val)
            dive(node.right)

        
        dive(root)
        
        return arr[k - 1]



