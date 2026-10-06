class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        
        def dfs(r, c, memo):
            if r == m - 1 and c == n - 1:
                return 1
            
            if not (0 <= r < m and 0 <= c < n):
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            total = 0
            total += dfs(r + 1, c, memo)
            total += dfs(r, c + 1, memo)
            
            memo[(r, c)] = total
            return memo[(r, c)]
        
        return dfs(0, 0, {})




        