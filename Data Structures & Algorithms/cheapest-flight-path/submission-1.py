class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[]*n for i in range(n)]
        for s,t,c in flights:
            adj[s].append((t,c))
        def dfs(node,cost,k):
            print(node,cost,k)
            if node == dst:
                print(node)
                return cost

            if k < 0:
                return float('inf')
            
            return min(dfs(t,c + cost,k-1) for t,c in adj[node] ) if adj[node] else float('inf')

        res = dfs(src,0,k)  
        return res if res != float('inf') else -1 
            

