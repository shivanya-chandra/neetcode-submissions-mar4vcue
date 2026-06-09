# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def revert(self, rt: TreeNode):
        if(not rt):
            return None
        temp1 = rt.left
        temp2= rt.right
        rt.left = temp2
        rt.right = temp1
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.revert(root)
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root