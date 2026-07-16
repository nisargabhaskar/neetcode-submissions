# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def diameter(node):
            nonlocal res
            if node is None:
                return 0
            res = max(res,diameter(node.left) + diameter(node.right) )
            return max(diameter(node.left) , diameter(node.right)) + 1
        diameter(root)
        return res