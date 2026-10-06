class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        
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
            

            


        