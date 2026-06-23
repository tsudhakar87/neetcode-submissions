class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_idx = 0

        for i in range(len(prices)):
            if prices[i] < prices[min_idx]:
                min_idx = i
            elif prices[i] - prices[min_idx] > res:
                res = prices[i] - prices[min_idx]

        return res