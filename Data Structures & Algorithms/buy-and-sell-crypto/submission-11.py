class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        n = len(prices)
        high = low = 0
        
        while high < n:
            if prices[high] <= prices[low]:
                low = high
            
            total = max(total, prices[high] - prices[low])
            high += 1
        
        return total