class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        if not prices:
            return 0
        
        buy = sell = 0

        while sell < n:
            if prices[sell] < prices[buy]:
                buy = sell
            
            profit = prices[sell] - prices[buy]
            maxProfit = max(profit, maxProfit)

            sell += 1
        
        return maxProfit
        