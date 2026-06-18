# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(rt, low, high):
            if not rt:
                return True
            if not(low < rt.val < high):
                return False
            return dfs(rt.left, low, rt.val) and dfs(rt.right, rt.val, high)
        
        return dfs(root, float("-inf"), float("inf"))
       
        
        



        