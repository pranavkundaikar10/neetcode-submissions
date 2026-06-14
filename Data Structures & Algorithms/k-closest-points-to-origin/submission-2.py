class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for pt in points:
            d = math.sqrt(pt[0]**2+pt[1]**2)
            heapq.heappush_max(heap, (d, pt))
            if len(heap) > k:
                heapq.heappop_max(heap)
        res = []
        for i in heap:
            res.append(i[1])
        return res
