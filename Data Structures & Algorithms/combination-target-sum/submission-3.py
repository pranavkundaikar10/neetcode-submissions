class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sum = 0
        def dfs(i, tmp, sum):
            if sum > target or i > len(nums)-1:
                return
            if sum == target:
                res.append(list(tmp))
                return
            tmp.append(nums[i])
            dfs(i, tmp, sum + nums[i])
            tmp.pop()
            dfs(i+1, tmp, sum)

        
        dfs(0, [], 0)
        return res
        