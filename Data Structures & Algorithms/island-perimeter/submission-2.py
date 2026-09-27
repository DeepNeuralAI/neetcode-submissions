class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            total = 0
            
            if not (0 <= r < ROWS and 0 <= c < COLS) or (grid[r][c] == 0):
                return 1
            
            visited.add((r, c))
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r_ = r + dr
                c_ = c + dc

                if (r_, c_) not in visited:
                    total += dfs(r_, c_)
            
            return total
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    total = dfs(r, c)
        
        return total

                
            
          
            
        