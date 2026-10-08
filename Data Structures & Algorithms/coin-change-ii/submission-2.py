class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Bottom Up Approach
        ROWS, COLS = len(coins), (amount + 1)
        dp = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            dp[r][0] = 1
        
        for c in range(1, COLS):
            if c - coins[0] >= 0:
                dp[0][c] = dp[0][c - coins[0]]
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                dp[r][c] = dp[r - 1][c]

                if c - coins[r] >= 0:
                    dp[r][c] += dp[r][c - coins[r]]
        
        return dp[ROWS - 1][COLS - 1]


        
        def ways(i, target, memo):
            if target == 0:
                return 1
            
            if i == len(coins) or amount < 0:
                return 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            c1 = 0
            if target - coins[i] >= 0:
                c1 = ways(i, target - coins[i], memo)
            
            c2 = ways(i + 1, target, memo)
            memo[(i, target)] = c1 + c2
            return memo[(i, target)]
        
        return ways(0, amount, {})
        

        
        