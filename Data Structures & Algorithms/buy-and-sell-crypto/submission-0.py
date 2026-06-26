class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        if not prices:
            return 0
        
        mini = prices[0]
        for i in range(1, n):
            profit = prices[i] - mini
            mini = min(mini, prices[i])
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
