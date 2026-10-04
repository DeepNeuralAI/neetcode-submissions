class Solution:
    def integerBreak(self, n: int) -> int:
        # Bottom Up
        dp = [0] * (n + 1)

        if n <= 2:
            return 1

        for i in range(3):
            dp[i] = 1
        
        for i in range(3, len(dp)):
            for j in range(1, i):
                dp[i] = max(
                    dp[i],
                    j * dp[i - j],
                    j * (i - j)
                )
        return dp[n]

            
