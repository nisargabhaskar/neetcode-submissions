# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max_val):
            if node is None:
                return 0
            left =  dfs(node.left,max(max_val,node.val))
            right = dfs(node.right,max(max_val,node.val))
            if node.val >= max_val:
                return 1 + left + right
            return left + right
        return dfs(root,-float('inf'))