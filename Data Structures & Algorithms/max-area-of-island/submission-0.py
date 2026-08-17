from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        maxArea = 0

        def bfs(node):
            r, c = node
            
            q = deque([node])
            visited.add(node)
            area = 0

            while q:
                r, c = q.popleft()
                area += 1

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r_ = r + dr
                    c_ = c + dc

                    if (r_, c_) in visited:
                        continue
                    
                    if not (0 <= r_ < ROWS and 0 <= c_ < COLS):
                        continue
                    
                    if grid[r_][c_] == 1:
                        visited.add((r_, c_))
                        q.append((r_, c_))
            
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = bfs((r, c))
                    maxArea = max(area, maxArea)
        return maxArea
                

                

                
                





            

        