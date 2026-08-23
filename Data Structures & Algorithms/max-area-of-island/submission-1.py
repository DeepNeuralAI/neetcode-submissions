class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxArea = 0
        
        def dfs(node):
            r, c = node
            visit.add(node)

            count = 1
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                r_ = r + dr
                c_ = c + dc

                if (not(0 <= r_ < ROWS and 0 <= c_ < COLS) or
                    grid[r_][c_] == 0 or
                    (r_, c_) in visit):
                    continue
                
                count += dfs((r_, c_))
            
            return count
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = dfs((r, c))
                    maxArea = max(maxArea, area)

        return maxArea

        