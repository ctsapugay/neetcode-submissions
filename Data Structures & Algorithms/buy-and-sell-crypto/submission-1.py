class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 0, 0
        for i, p in enumerate(prices):
            profit = max(profit, p - prices[buy])
            if p < prices[buy]:
                buy = i
        return profit
        