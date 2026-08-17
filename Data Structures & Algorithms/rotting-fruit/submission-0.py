from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh_count = 0
        time = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((0, r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        def bfs():
            nonlocal time, fresh_count
            
            while queue:
                t, x, y = queue.popleft()
                time = max(time, t)

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r_ = x + dr
                    c_ = y + dc

                    if not (0 <= r_ < ROWS and 0 <= c_ < COLS):
                        continue
                    
                    if grid[r_][c_] == 0:
                        continue
                    
                    if grid[r_][c_] == 1:
                        grid[r_][c_] = 2
                        fresh_count -= 1
                        queue.append((t + 1, r_, c_))
        
       
        bfs()
        return time if fresh_count == 0 else -1


        