# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = [True]

        def dive(node, l, r):
            if node is None:
                return
            
            if node.val < r and node.val > l:
                dive(node.left, l, node.val)
                dive(node.right, node.val, r)
            else:
                ans[0] = False
        
        dive(root.left, -1001, root.val)
        dive(root.right, root.val, 1001)

        return ans[0]