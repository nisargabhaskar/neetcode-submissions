
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = nums[0]
        while num < len(nums):
            if nums[num] == num:
                return num
            else:
                temp = nums[num]
                nums[num] = num
                num = temp