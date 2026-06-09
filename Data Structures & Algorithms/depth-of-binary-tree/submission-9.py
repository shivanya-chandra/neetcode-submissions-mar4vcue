# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def count(self, rt: TreeNode):
        c=0
        if(not rt):
            return 0
        leftDepth = self.count(rt.left)
        rightDepth = self.count(rt.right)
        return 1 + max(leftDepth, rightDepth)
    def maxDepth(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.count(root)
        
        
        