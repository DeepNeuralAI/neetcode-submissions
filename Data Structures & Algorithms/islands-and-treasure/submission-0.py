from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        
        def bfs(q):
            while q:
                d, x, y = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r_ = x + dr
                    c_ = y + dc

                    if not (0 <= r_ < ROWS and 0 <= c_ < COLS):
                        continue
                    
                    if grid[r_][c_] == -1:
                        continue
                    
                    if grid[r_][c_] == INF:
                        grid[r_][c_] = d + 1
                        q.append((d + 1, r_, c_))
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((0, r, c))
        
        bfs(q)
        