# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder => RoLR
        #inorder => LRoR
        def dfs(preorder,inorder):
            if preorder and inorder:
                root = TreeNode(preorder[0])
                idx_inorder = inorder.index(preorder[0])
                root.left  = dfs(preorder[1:1+idx_inorder],inorder[:idx_inorder])
                root.right = dfs(preorder[1+idx_inorder:],inorder[idx_inorder+1:])
                return root
            return None
        return dfs(preorder,inorder)