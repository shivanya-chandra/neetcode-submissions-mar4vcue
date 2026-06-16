# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trav(self, rt, l):
        if not rt:
            l.append(None)
            return None
        
        self.trav(rt.left, l)
        l.append([rt.val, "left"])
        self.trav(rt.right, l)
        l.append([rt.val, "right"])

        return rt
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.t1 = []
        self.t2 = []
        self.trav(p, self.t1)
        print(self.t1)
        self.trav(q, self.t2)
        print(self.t2)

        return self.t1 == self.t2
        