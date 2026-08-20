class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(node, visit):
            visit.add(node)
            r, c = node

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r_ = r + dr
                c_ = c + dc

                if (not (0 <= r_ < ROWS and 0 <= c_ < COLS) 
                    or (r_, c_) in visit 
                    or heights[r_][c_] < heights[r][c]):
                    continue
                
                dfs((r_, c_), visit)
            
        
        for r in range(ROWS):
            dfs((r, 0), pac)
            dfs((r, COLS - 1), atl)
        
        for c in range(COLS):
            dfs((0, c), pac)
            dfs((ROWS - 1, c), atl)
        
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
