class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]

        ctr = defaultdict(int)
        for i in nums:
            ctr[i] += 1
        
        for key, val in ctr.items():
            freq[val].append(key)

        res = []
        i = len(freq) - 1
        while i >= 0:
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
            i -= 1