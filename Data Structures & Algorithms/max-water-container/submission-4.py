class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        res = 0
        while i < j:
            amount = min(heights[i], heights[j]) * abs(i-j)
            print(f'i {i}, j {j}, amount {amount}')
            res = max(amount, res)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return res