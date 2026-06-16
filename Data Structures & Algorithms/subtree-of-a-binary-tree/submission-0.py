# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, rt, subRt):
        if not rt and not subRt: 
            return True
        if not rt or not subRt:
            return False
        if rt.val != subRt.val:
            return False

        return self.sameTree(rt.left, subRt.left) and self.sameTree(rt.right, subRt.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(not root):
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        