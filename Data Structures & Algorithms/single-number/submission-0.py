class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for x in nums:
            if x not in seen:
                seen[x] = 1
            else :
                seen[x] += 1
        return [x for x,y in seen.items() if y ==1 ][0]