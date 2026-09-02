class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        start = 0
        visited = [start]
        def dfs(start,parent):
            res = True
            for node in graph[start]:
                if node == parent:
                    pass
                elif node in visited:
                    print(node)
                    return False
                else:
                    visited.append(node)
                    res = res and dfs(node,start)
                    if not res:
                        print(node,start)
                        return False
            return res
        
        if dfs(start,-1) and len(visited) == n:
            return True
        print(len(visited),visited)
        return False