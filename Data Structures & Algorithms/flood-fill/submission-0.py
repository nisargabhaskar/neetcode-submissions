class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        visited = []
        def dfs(image ,sr ,sc ,color):
            old_color = image[sr][sc]
            image[sr][sc] = color
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            visited.append((sr,sc))
            for nr,nc in directions:
                if sr + nr >= 0 and sr + nr < ROWS and sc + nc >= 0 and sc+nc < COLS and image[sr + nr][sc + nc] == old_color and (sr + nr, sc + nc) not in visited:
                    dfs(image,sr + nr,sc + nc,color)
        dfs(image, sr, sc, color)
        return image