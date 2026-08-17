class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        def dfs(node):
            x, y = node
            visited.add(node)

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r_ = x + dr
                c_ = y + dc

                if (r_, c_) in visited:
                    continue
                
                if not (0 <= r_ < ROWS and 0 <= c_ < COLS):
                    continue
                
                if grid[r_][c_] == '1':
                    dfs((r_, c_))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == '1':
                    dfs((r, c))
                    count += 1
        return count