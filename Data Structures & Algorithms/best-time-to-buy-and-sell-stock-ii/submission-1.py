class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(prices, 0, 1, {})
    



    def solve(self, prices, i, canBuy = 1, memo = {}):
        if i == len(prices):
            return 0
        
        if (i, canBuy) in memo:
            return memo[(i, canBuy)]
        
        if canBuy:
            memo[(i, canBuy)] = max(
                -prices[i] + self.solve(prices, i + 1, canBuy = 0, memo = memo),
                self.solve(prices, i + 1, canBuy, memo)
            )
        else:
            memo[(i, canBuy)] = max(
                prices[i] + self.solve(prices, i + 1, canBuy = 1, memo = memo),
                self.solve(prices, i + 1, canBuy, memo)
            )
        
        return memo[(i, canBuy)]


        