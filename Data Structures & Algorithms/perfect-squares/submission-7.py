class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for i in range(2, len(dp)):
            for j in range(1, i + 1):
                if j * j > i:
                    break
                
                dp[i] = min(
                    dp[i],
                    1 + dp[i - (j * j)]
                )

        return dp[n]



       