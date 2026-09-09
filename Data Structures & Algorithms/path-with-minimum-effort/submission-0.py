from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
    

        def dijkstra():
            ROWS, COLS = len(heights), len(heights[0])
            dist = [[float('inf')] * COLS for _ in range(ROWS)]
            dist[0][0] = 0
            heap = []
            heappush(heap, (0, 0, 0))
            

            while heap:
                path_effort, r, c = heappop(heap)

                if r == ROWS - 1 and c == COLS - 1:
                    return path_effort

                for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    r_ = r + dr
                    c_ = c + dc

                    if not (0 <= r_ < ROWS and 0 <= c_ < COLS): continue
   
                    new_effort = max(path_effort, abs(heights[r_][c_] - heights[r][c]))

                    if new_effort < dist[r_][c_]:
                        dist[r_][c_] = new_effort
                        heappush(heap, (new_effort, r_, c_))


            return -1

        return dijkstra()