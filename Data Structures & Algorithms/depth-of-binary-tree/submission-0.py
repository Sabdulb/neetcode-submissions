# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = [0]

        def dive(node, val):

            if node is None:
                return

            val += 1

            count[0] = max(count[0], val)

            dive(node.left, val)
            dive(node.right, val)

        dive(root, 0)

        return count[0]

            
        