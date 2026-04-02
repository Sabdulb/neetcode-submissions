# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mp = []
        return self.dfs(root,p,q,mp)


    def dfs(self,root,p,q,mp):
        ans = None
        left = []
        right = []
        if root.left:
            ans = self.dfs(root.left,p,q,left)
            if ans: return ans
        if root.right:
            ans = self.dfs(root.right,p,q,right)
            if ans:
                return ans
        
        for val in left:
            mp.append(val)
        for val in right:
            mp.append(val)
        mp.append(root.val)
        
        if q.val in mp and p.val in mp:
            return root