# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = [-1001]

        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            ret = max(left + node.val, right + node.val, node.val)

            temp = max(right + node.val + left, node.val, max(right, left) + node.val)

            ans[0] = max(ans[0], temp)

            return ret
        
        dfs(root)

        return ans[0]