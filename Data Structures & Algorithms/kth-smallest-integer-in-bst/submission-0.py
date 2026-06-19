# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.c = 0
        self.v = root.val
        def dfs(rt, k):
            if not rt:
                return None

            
            
            dfs(rt.left, k)
            self.c += 1
            
            if(self.c == k):
                self.v = rt.val
            dfs(rt.right,k)
            
            return self.v
           

        return dfs(root, k)
     
        