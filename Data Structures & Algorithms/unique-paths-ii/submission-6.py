class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        # Bottom Up Approach
        dp = [[0] * COLS for _ in range(ROWS)]
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp[0][0] = 1
        # Precompute First Row
        for c in range(1, COLS):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c - 1]
        
        for r in range(1, ROWS):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r - 1][0]
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[ROWS - 1][COLS - 1]
        
        def dfs(r, c, memo):
            if (not (0 <= r < ROWS and 0 <= c < COLS) 
                or obstacleGrid[r][c] == 1):
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] = dfs(r + 1, c, memo) + dfs(r, c + 1, memo)
            return memo[(r, c)]
        
        return dfs(0, 0, {})
            

            


        