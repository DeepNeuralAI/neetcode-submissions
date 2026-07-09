class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        current_min = float('inf')
        maxProfit = 0

        l = r = 0
        while r < n:
            if prices[r] < prices[l]:
                l = r
            else:
                maxProfit = max(prices[r] - prices[l], maxProfit)
            r += 1
        return maxProfit

            
        