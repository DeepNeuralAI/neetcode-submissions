class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom Up
        dp = [[float('inf')] * (amount + 1) for _ in range(len(coins))]

        # Set number of coins to 0 for amount 0
        for i in range(len(coins)):
            dp[i][0] = 0
        
        # Pre-compute amount for denomination of first coin
        for c in range(1, amount + 1):
            if c - coins[0] >= 0:
                dp[0][c] = 1 + dp[0][c - coins[0]]

        for i in range(1, len(coins)):
            for amt in range(1, amount + 1):
                dp[i][amt] = dp[i - 1][amt]
                
                if amt - coins[i] >= 0:
                    dp[i][amt] = min(
                        1 + dp[i][amt - coins[i]],
                        dp[i][amt]
                    )
        
        res = dp[len(coins) - 1][amount]
        return -1 if res == float('inf') else res

        