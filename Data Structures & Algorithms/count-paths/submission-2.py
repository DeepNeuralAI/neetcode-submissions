class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        # Bottom Up Approach
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1

        # Precompute last row
        for c in range(COLS - 2, -1, -1):
            dp[ROWS - 1][c] = dp[ROWS - 1][c + 1]
        
        for r in range(ROWS - 2, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] = (
                    dp[r + 1][c] +
                    (dp[r][c + 1] if c + 1 < COLS else 0)
                )
        
        return dp[0][0]

        
        def dfs(r, c, memo):
            if r == m - 1 and c == n - 1:
                return 1
            
            if not (0 <= r < m and 0 <= c < n):
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            total = 0
            total += dfs(r + 1, c, memo)
            total += dfs(r, c + 1, memo)
            
            memo[(r, c)] = total
            return memo[(r, c)]
        
        return dfs(0, 0, {})




        