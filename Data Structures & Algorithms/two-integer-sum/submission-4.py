class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            n = nums[i]
            if target - n in hash_map:
                return [hash_map[target - n] ,i]
            else :
                hash_map[n] = i
