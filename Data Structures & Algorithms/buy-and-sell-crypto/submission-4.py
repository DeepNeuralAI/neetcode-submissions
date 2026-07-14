class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window
        profit = 0
        n = len(prices)
        
        l = r = 0
        while r < n:
            if prices[r] < prices[l]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
            r += 1
        
        return profit

        