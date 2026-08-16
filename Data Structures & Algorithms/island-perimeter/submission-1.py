
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(node):
            r, c = node
            visited.add((r, c))

            count = 0
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                r_ = r + dr
                c_ = c + dc

                if not (0 <= r_ < ROWS and 0 <= c_ < COLS):
                    count += 1
                    continue
                
                if grid[r_][c_] == 0:
                    count += 1
                    continue
                
                if (r_, c_) in visited:
                    continue
                
                count += dfs((r_, c_))

            return count
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    perimeter += dfs((r, c))

        return perimeter
