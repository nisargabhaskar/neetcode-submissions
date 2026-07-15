class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            
            if (node1 and not node2) or (node2 and not node1):
                return False
            
            return (
                node1.val == node2.val and
                dfs(node1.left, node2.left) and
                dfs(node1.right, node2.right)
            )
        
        return dfs(p, q)