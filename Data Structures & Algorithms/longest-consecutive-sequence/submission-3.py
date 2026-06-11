class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, seq_len = 0, defaultdict(int)
        for num in nums:
            if seq_len.get(num):
                continue
            sl = seq_len.get(num-1, 0) + seq_len.get(num+1, 0) + 1
            seq_len[num] = sl
            res = max(res, sl)
            seq_len[num - seq_len.get(num-1, 0)] = sl
            seq_len[num + seq_len.get(num+1, 0)] = sl
        return res