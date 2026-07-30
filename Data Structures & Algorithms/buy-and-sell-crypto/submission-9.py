class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        r = total = 0
        n = len(prices)
        min_seen = float('inf')

        while r < n:
            min_seen = min(prices[r], min_seen)
            total = max(total, prices[r] - min_seen)
            r += 1
        
        return total
