class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        

        def dfs(perm: List[int], pick: List[bool]):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    dfs(perm, pick)
                    perm.pop()
                    pick[i] = False
        dfs([], [False] * len(nums))

        return res