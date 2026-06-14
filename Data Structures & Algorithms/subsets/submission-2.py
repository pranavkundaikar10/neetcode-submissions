class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, tmp):
            if i > len(nums) - 1:
                res.append(list(tmp))
                return
            tmp.append(nums[i])
            dfs(i+1, tmp)
            tmp.pop()
            dfs(i+1, tmp)
        dfs(0, [])

        return res

