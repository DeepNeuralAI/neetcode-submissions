class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # # Bottom Up:
        # ROWS, COLS = len(s) + 1, len(t) + 1
        # dp = [[0] * COLS for _ in range(ROWS)]
        
        # for r in range(ROWS):
        #     dp[r][0] = 1
        
        # for r in range(1, ROWS):
        #     for c in range(1, COLS):
        #         if s[r - 1] == t[c - 1]:
        #             dp[r][c] += dp[r - 1][c - 1]
                
        #         dp[r][c] += dp[r - 1][c]
        
        # return dp[ROWS - 1][COLS - 1]
        
        def num_ways(i, j, memo):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
           
            c1 = 0
            if i < len(s) and j < len(t) and s[i] == t[j]:
                c1 = num_ways(i + 1, j + 1, memo)
            
            c2 = num_ways(i + 1, j, memo)
            memo[(i, j)] =  c1 + c2
            return memo[(i, j)]
        
        return num_ways(0, 0, {})
        



        