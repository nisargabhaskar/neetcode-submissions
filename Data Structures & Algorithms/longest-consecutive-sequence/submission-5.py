class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(set(nums))
        length = 1
        maxlength = 0
        for x in range(len(nums)-1):
            if nums[x] +1 == nums[x+1]:
                length += 1
            else:
                if maxlength < length:
                    maxlength = length
                length = 1
                print(maxlength,nums[:x])
        if maxlength < length:
                maxlength = length
        return maxlength 