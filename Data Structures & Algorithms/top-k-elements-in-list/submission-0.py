class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        return [x[0] for x in sorted(count.items(), key=lambda item: item[1])[-k:]]