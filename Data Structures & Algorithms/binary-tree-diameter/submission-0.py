# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def count(rt):
            if not rt:
                return 0

            leftDepth = count(rt.left)
            rightDepth = count(rt.right)

            # longest path THROUGH this node
            self.diameter = max(self.diameter, leftDepth + rightDepth)

            # return height of this node
            return 1 + max(leftDepth, rightDepth)

        count(root)
        return self.diameter
        