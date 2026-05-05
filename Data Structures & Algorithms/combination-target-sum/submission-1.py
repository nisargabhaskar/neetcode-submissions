class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sumlist = [],[]
        def dfs(i):
            if sum(sumlist) == target:
                res.append(sumlist.copy())
                return
            if i >= len(nums) or sum(sumlist) > target:
                return
            
            sumlist.append(nums[i])
            dfs(i)
            sumlist.pop()
            dfs(i+1)
        dfs(0)
        return res