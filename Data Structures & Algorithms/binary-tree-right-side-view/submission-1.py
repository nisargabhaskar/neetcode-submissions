# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def bfs(node,level):
            if node is None:
                return
            if len(res)== level:
                res.append([])
            res[level].append(node.val)
            bfs(node.left,level + 1)
            bfs(node.right,level + 1)
        bfs(root,0)
        return [x[-1] for x in res]