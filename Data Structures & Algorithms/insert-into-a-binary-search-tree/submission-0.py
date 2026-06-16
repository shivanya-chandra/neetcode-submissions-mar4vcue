# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        l = False
        r = False
        if(not root):
            print("hello")
            return TreeNode(val)
        if root.val < val:
            
            root.right = self.insertIntoBST(root.right, val)
    
            print("hello1", root.val)
        else:
            
            root.left = self.insertIntoBST(root.left, val)
            # if(not root.right):
            #     root.right = TreeNode(val)


        return root
        