"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        init = {node.val: Node(node.val)} 
        graph = []
        def get_neighbors(node):
            neighbors = []
            for n in node.neighbors:
                if n.val not in init:
                    init[n.val] = Node(n.val)
                    init[n.val].neighbors = get_neighbors(n)
                neighbors.append(init[n.val]) 
            return neighbors
        init[node.val].neighbors = get_neighbors(node)
        return init[node.val]