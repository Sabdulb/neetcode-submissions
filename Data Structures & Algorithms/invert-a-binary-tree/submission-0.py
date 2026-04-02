# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if not node:
                return
            temp1 = node.left
            temp2 = node.right

            node.left = temp2
            node.right = temp1

            invert(node.left)
            invert(node.right)
        
        invert(root)

        return root
