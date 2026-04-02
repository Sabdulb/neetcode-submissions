# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        mp = defaultdict(set)

        def dive(node):

            if node is None:
                return set()
            
            temp = set()

            temp.update(dive(node.left))
            temp.update(dive(node.right))
            
            temp.add(node.val)

            mp[node] = temp

            return temp
        
        dive(root)

        print(mp)
        ans = None

        for key in mp.keys():
            print(key.val)
            print(mp[key])
            if p.val in mp[key] and q.val in mp[key]:
                print("here")
                if ans is None:
                    ans = key
                else:
                    if len(mp[key]) <= len(mp[ans]):
                        ans = key
        
        return ans
            
            


