import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        def bfs():
            pq = []
            heapq.heappush(pq, (grid[0][0], 0, 0))

            while pq:
                curr_path_time, x, y = heapq.heappop(pq)

                if x == ROWS - 1 and y == COLS - 1:
                    return curr_path_time
                
                if (x, y) in visited:
                    continue
                
                visited.add((x, y))
                for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                    x_ = x + dx
                    y_ = y + dy

                    if ((0 <= x_ < ROWS and 0 <= y_ < COLS) and (x_, y_) not in visited):
                        new_path_time = max(curr_path_time, grid[x_][y_])
                        heapq.heappush(pq, (new_path_time, x_, y_))
            return
        

        return bfs()