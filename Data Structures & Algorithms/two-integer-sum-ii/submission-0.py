class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lidx = len(numbers)
        sidx = 1
        while sidx < lidx:
            if numbers[lidx-1] + numbers[sidx -1] > target:
                lidx -= 1
            elif numbers[lidx-1] + numbers[sidx -1] < target:
                sidx += 1
            else :
                if lidx!=sidx :
                    return [sidx,lidx]