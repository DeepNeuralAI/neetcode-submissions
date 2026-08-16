from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(root):
            q = deque([root])
            visited.add(root)
            total = 0

            while q:
                r, c = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    r_ = r + dr
                    c_ = c + dc

                    if not (0 <= r_ < ROWS and 0 <= c_ < COLS) or grid[r_][c_] == 0:
                        total += 1
                        continue
                    
                    if (r_, c_) in visited:
                        continue
                    
                    visited.add((r_, c_))
                    q.append((r_, c_))
            
            return total

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    perimeter += bfs((r, c))
        
        return perimeter
