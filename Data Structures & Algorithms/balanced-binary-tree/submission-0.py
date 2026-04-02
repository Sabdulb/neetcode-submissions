# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ans = [True]

        def dive(node, k):
            if node is None:
                return True

            l = dive(node.left, k)
            r = dive(node.right, k)

            if abs(l - r) > 1:
                ans[0] = ans[0] & False
            
            return max(l + 1, r + 1)
        
        dive(root, 0)

        return ans[0]

