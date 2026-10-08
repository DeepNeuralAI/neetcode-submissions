class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit(i, sell) - maximum profit from i...nth day
        # Bottom Up Approach
        ROWS, COLS = len(prices), 2
        dp = [[0] * COLS for _ in range(ROWS + 1)]

        for i in range(ROWS - 1, -1, -1):
            # 0 - Can Buy / Not Sell
            # 1 - Can Sell / Not Buy
            for canBuy in range(2):
                if canBuy == 0:
                    dp[i][canBuy] = -prices[i] + dp[i + 1][1 - canBuy]
                else:
                    dp[i][canBuy] = prices[i] + (dp[i + 2][1 - canBuy] if i + 2 <= ROWS else 0)
                dp[i][canBuy] = max(
                    dp[i][canBuy],
                    dp[i + 1][canBuy]
                )
        
        return dp[0][0]
                

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

        