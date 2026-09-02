class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            for nei in graph[node]:
                if nei in visited:
                    pass
                else:
                    visited.append(nei)
                    dfs(nei)
        graph = [[] for _ in range(n)]
        visited = []
        count = 0
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if i not in visited:
                visited.append(i)
                count  += 1
                dfs(i)
        return count