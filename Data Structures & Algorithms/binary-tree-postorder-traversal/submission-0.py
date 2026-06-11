# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, rt, l):
        if not rt:
            return None
        
        self.recurse(rt.left,l)
        self.recurse(rt.right,l)
        l.append(rt.val)
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        self.recurse(root,l)
        return l
        