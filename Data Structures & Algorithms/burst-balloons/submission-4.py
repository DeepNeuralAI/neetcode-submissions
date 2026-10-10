class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0

        balloons = [1] + nums + [1]
        # Bottom Up Approach
        ROWS, COLS = len(balloons), len(balloons)
        dp = [[0] * COLS for _ in range(ROWS)]
        
        n = len(nums)
        for offset in range(n):
            for r in range(1, n - offset + 1):
                c = r + offset
                for k in range(r, c + 1):
                    value = balloons[r - 1] * balloons[k] * balloons[c + 1]
                    dp[r][c] = max(
                        dp[r][c],
                        value + dp[r][k - 1] + dp[k + 1][c]
                    )
        return dp[1][n]

                    

        def max_coins(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == j:
                return balloons[i - 1] * balloons[i] * balloons[i + 1]
            
            if i > j:
                return 0
            
            
            res = 0
            for k in range(i, j + 1):
                value = balloons[i - 1] * balloons[k] * balloons[j + 1]
                subproblem = max_coins(i, k - 1, memo) + max_coins(k + 1, j, memo)
                res = max(res, value + subproblem)
            memo[(i, j)] = res
            return res
        
        return max_coins(1, len(nums), {})

        
