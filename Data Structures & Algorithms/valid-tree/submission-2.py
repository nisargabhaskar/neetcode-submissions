class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        graph = [[] for _ in range(n)]
        for r,c in edges:
            graph[r].append(c)
            graph[c].append(r)
        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)

        while q:
            node, parent = q.popleft()
            for nn in graph[node]:
                if nn == parent:
                    continue
                if nn not in visit:
                    visit.add(nn)
                    q.append((nn,node))
                else:
                    return False
        return len(visit) == n
