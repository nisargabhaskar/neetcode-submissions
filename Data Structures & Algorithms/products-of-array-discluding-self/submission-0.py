class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for x in range(len(nums)):
            prod = 1
            for y in range(len(nums)):
                if x == y:
                    continue
                prod *= nums[y]
            output.append(prod)
        return output