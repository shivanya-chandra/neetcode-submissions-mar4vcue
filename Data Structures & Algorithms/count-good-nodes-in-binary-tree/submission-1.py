# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def count(self, rt):
        # if not rt:
        #     return None
        # self.count(rt.right)
        # self.count(rt.left)
        # print(rt.val)
        # return rt.val
    def goodNodes(self, root: TreeNode) -> int:
        visited = []

        def dfs(maxVal, rt):
            if not rt:
                return 0

            res = 1 if rt.val >= maxVal else 0
            maxVal = max(maxVal, rt.val)
            res +=  dfs(maxVal, rt.right)
            res += dfs(maxVal, rt.left)

            return res
        return dfs(root.val, root)
       
        