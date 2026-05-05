# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = root.val
        def dfs(root):
            nonlocal maxsum
            if not root :
                return 0
            else:
                rsum = max(0,dfs(root.right))
                lsum = max(0,dfs(root.left))
                maxsum = max( rsum + root.val + lsum,maxsum)
                return root.val +max(lsum,rsum)
        dfs(root)
        return maxsum