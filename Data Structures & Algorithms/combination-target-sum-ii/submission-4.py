class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, subset = [], []
        def dfs(i, sum):
            if sum == target:
                res.append(list(subset))
                return
            if sum > target or i > len(candidates) - 1:
                return
            subset.append(candidates[i])
            dfs(i+1, sum + candidates[i])
            subset.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, sum)

                
        dfs(0,0)
        return res
