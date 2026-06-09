class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j, res = 0, 0, 0

        while j < len(prices):
            profit = prices[j] - prices[i]
            res = max(profit, res)
            if prices[j] < prices[i]:
                i = j
            j += 1
        return res


        