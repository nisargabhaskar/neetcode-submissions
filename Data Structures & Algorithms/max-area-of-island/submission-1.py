class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def explore_island(grid,r,c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            area = 0
            grid[r][c] = 0
            for dr,dc in directions:
                area += explore_island(grid,r+dr,c+dc)
            return 1 + area
        max_area = 0
        for r in range(ROWS):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = explore_island(grid,r,c)
                    max_area = max(max_area,area)
        return max_area