class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
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

            
        