class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Bottom Up Approach
        ROWS, COLS = len(word1) + 1, len(word2) + 1
        dp = [[float('inf')] * COLS for _ in range(ROWS)]
        dp[0][0] = 0
        
        for r in range(1, ROWS):
            dp[r][0] = r
        
        for c in range(1, COLS):
            dp[0][c] = c
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                    continue
                
                insert = dp[r][c - 1]
                delete = dp[r - 1][c]
                replace = dp[r - 1][c - 1]
                dp[r][c] = 1 + min(insert, delete, replace)
        
        return dp[ROWS - 1][COLS - 1]

        def operations(i, j, memo):
            if j == len(word2):
                return len(word1) - i
            
            if i == len(word1):
                return len(word2) - j
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                return operations(i + 1, j + 1, memo)
            
            insert = operations(i, j + 1, memo)
            delete = operations(i + 1, j, memo)
            replace = operations(i + 1, j + 1, memo)

            memo[(i, j)] = 1 + min(insert, delete, replace)
            return memo[(i, j)]
        
        return operations(0, 0, {})
            

            

        