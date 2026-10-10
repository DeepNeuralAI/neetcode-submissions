class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        # Bottom Up
        cells = [(matrix[r][c], r, c) for c in range(COLS) for r in range(ROWS)]
        cells.sort(reverse = True)
        dp = [[0] * COLS for _ in range(ROWS)]
        res = 0

        for (value, r, c) in cells:
            best = 0
            for dr, dc in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                r_ = r + dr
                c_ = c + dc
                if 0 <= r_ < ROWS and 0 <= c_ < COLS:
                    if matrix[r_][c_] > matrix[r][c]:
                        best = max(best, dp[r_][c_])
            dp[r][c] = 1 + best
            res = max(dp[r][c], res)
        
        return res

        def longest_path(r, c, memo):
            if (r, c) in memo:
                return memo[(r, c)]
            
            best = 0
            for dr, dc in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                r_ = r + dr
                c_ = c + dc
                if 0 <= r_ < ROWS and 0 <= c_ < COLS:
                    if matrix[r_][c_] > matrix[r][c]:
                        best = max(best, longest_path(r_, c_, memo))
                
            memo[(r, c)] = 1 + best
            return memo[(r, c)]
        
        res = 0
        memo = {}
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, longest_path(r, c, memo))
        return res
        
        
                

            