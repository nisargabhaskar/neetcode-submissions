class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = [-n for n in nums]
        heapq.heapify(res)
        while k > 0:
            a = heapq.heappop(res)
            k -= 1
        return -a