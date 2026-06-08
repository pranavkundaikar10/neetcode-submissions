class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = {}
        for num in nums:
            ctr[num] = ctr.get(num, 0) + 1

        heap = []
        for key, val in ctr.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in heap:
            res.append(i[1])
        return res
