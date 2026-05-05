# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxonroute):
            if not node :
                return 0
            if node.val >= maxonroute:
                return dfs(node.right,node.val) + dfs(node.left,node.val) + 1
            else:
                return dfs(node.right,maxonroute) + dfs(node.left,maxonroute)
        return dfs(root,root.val)