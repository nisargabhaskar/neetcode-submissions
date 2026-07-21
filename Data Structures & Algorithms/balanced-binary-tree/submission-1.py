# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return (True,0)
            left, left_height = dfs(node.left)
            right, right_height = dfs(node.right)
            if left and right and abs(left_height - right_height) <= 1:
                return (True,max(left_height,right_height)+1)
            else:
                return (False,0)
        return dfs(root)[0]