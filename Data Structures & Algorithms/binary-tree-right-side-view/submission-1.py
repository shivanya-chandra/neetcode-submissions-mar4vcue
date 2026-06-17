# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(rt, depth):
            if not rt:
                return []
            
            if len(res) == depth:
                res.append(rt.val)
            
            dfs(rt.right, depth + 1)
            dfs(rt.left, depth + 1)
            return res
        return dfs(root, 0)
    
        

         