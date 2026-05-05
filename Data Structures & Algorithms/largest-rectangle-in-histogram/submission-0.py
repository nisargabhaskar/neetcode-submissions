class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            l,r= i,i
            while r+1 < len(heights) and heights[i] <= heights[r+1]:
                r += 1
            while l> 0 and heights[i] <= heights[l-1]:
                l-= 1
            area = max(area, heights[i] * (r-l+1))
        return area