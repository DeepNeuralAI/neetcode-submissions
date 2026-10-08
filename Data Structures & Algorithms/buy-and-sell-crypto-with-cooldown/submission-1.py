class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit(i, sell) - maximum profit from i...nth day
        def profit(i, can_sell, memo):
            # can_sell: True - Already purchased
            # can_sell: False - Can make a purchase

            if i >= len(prices):
                return 0
            
            if (i, can_sell) in memo:
                return memo[(i, can_sell)]
            
            c1 = 0
            if not can_sell:
                c1 = -prices[i] + profit(i + 1, True, memo)
            else:
                c1 = prices[i] + profit(i + 2, False, memo)
            
            c2 = profit(i + 1, can_sell, memo)

            memo[(i, can_sell)] = max(c1, c2)
            return memo[(i, can_sell)]

        return profit(0, False, {})

        