# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def backtrack(node):
            if node is None:
                return 
            left = backtrack(node.left)
            right = backtrack(node.right)
            node.left = right
            node.right = left
            return node
        return backtrack(root)