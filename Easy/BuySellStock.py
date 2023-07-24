class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        sell = 1
        buy = 0
        while(sell<len(prices)):
            profit = prices[sell] - prices[buy]
            if prices[buy]>prices[sell]:
                buy = sell
            else:
                max_profit = max(max_profit, profit)
            sell = sell + 1
        return max_profit
