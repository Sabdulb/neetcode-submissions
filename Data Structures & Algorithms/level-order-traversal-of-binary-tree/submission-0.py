# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        mp = {}
        ans = []
        level = 1
        self.work(root,mp,level)
        for key in mp.keys():
            ans.append(mp.get(key))
        return ans

    def work(self,root,mp,level):
        if mp.get(level) is None:
            mp[level] = []
            mp[level].append(root.val)
        else:
            mp[level].append(root.val)
        if root.left: self.work(root.left,mp,level + 1)
        if root.right: self.work(root.right, mp, level + 1)


