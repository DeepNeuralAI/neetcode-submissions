class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        n = len(prices)
        if not prices:
            return 0

        mini = prices[0]
        res = 0

        for i in range(n):
            res = max(res, prices[i] - mini)
            mini = min(mini, prices[i])
        
        return res
            

        