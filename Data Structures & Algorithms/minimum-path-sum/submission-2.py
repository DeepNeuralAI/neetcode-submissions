class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # Bottom Up Approach
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = grid[0][0]

        # Precompute First Row
        for c in range(1, COLS):
            dp[0][c] = grid[0][c] + dp[0][c - 1]
        
        for r in range(1, ROWS):
            for c in range(COLS):
                top = dp[r - 1][c]
                left = dp[r][c - 1] if c - 1 >= 0 else float('inf')
                dp[r][c] = grid[r][c] + min(top, left)

        return dp[ROWS - 1][COLS - 1]
        
        def dfs(r, c, memo):
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]
            
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return float('inf')
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            c1 = dfs(r + 1, c, memo)
            c2 = dfs(r, c + 1, memo)
            
            memo[(r, c)] = grid[r][c] + min(c1, c2)
            return memo[(r, c)]
        
        return dfs(0, 0, {})

            
        