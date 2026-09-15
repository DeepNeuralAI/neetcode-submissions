class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        def bfs(q, visit):

            while q:
                r, c, node_height = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r_ = r + dr
                    c_ = c + dc

                    if not (0 <= r_ < ROWS and 0 <= c_ < COLS) or (r_, c_) in visit:
                        continue
                    
                    if heights[r_][c_] >= node_height:
                        visit.add((r_, c_))
                        q.append((r_, c_, heights[r_][c_]))
            
        pacific, atlantic = set(), set()
        for r in range(ROWS):
            pacific.add((r, 0))
            atlantic.add((r, COLS - 1))
        
        for c in range(COLS):
            pacific.add((0, c))
            atlantic.add((ROWS - 1, c))
        
        q = deque()
        for r, c in pacific:
            q.append((r, c, heights[r][c]))
        
        bfs(q, pacific)

        q = deque()
        for r, c in atlantic:
            q.append((r, c, heights[r][c]))
        
        bfs(q, atlantic)

        res = []
        for r, c in atlantic:
            if (r, c) in pacific:
                res.append([r, c])
        
        return res



        