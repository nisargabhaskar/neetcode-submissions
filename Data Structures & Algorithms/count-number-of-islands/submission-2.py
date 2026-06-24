class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def cover_island(r,c):
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            if r  < 0 or r>=len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for nr,nc in directions:
                cover_island(r+nr,c+nc)
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1':

                    count += 1
                    cover_island(i,j)
        return count