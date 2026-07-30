class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        l = r = total = 0
        n = len(prices)

        while r < n:
            if prices[r] < prices[l]:
                l = r
            else:
                total = max(total, prices[r] - prices[l])
            
            r += 1
        
        return total