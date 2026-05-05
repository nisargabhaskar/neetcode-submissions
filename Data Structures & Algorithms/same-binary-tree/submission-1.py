# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            lres = self.isSameTree(p.left,q.left)
            rres = self.isSameTree(p.right,q.right)
            if lres==True and rres ==True and p.val == q.val:
                return True
        if p is None and q is None:
            return True
        return False