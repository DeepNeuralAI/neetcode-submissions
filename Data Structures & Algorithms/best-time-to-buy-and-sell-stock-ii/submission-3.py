class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][1] = -prices[0]


        for i in range(1, n):
            for j in range(2):
                if j == 0:
                    dp[i][j] = max(
                        prices[i] + dp[i - 1][1 - j],
                        dp[i - 1][j]
                    )
                elif j == 1:
                    dp[i][j] = max(
                        -prices[i] + dp[i - 1][1 - j],
                        dp[i - 1][j]
                    )
        return dp[n - 1][0]



        