class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        ROWS, COLS = len(s1) + 1, len(s2) + 1
        # Bottom Up Approach
        dp = [[False] * COLS for _ in range(ROWS)]
        dp[0][0] = True

        for r in range(1, ROWS):
            if s1[r - 1] == s3[r - 1] and dp[r - 1][0]:
                dp[r][0] = True
        
        for c in range(1, COLS):
            if s2[c - 1] == s3[c - 1] and dp[0][c - 1]:
                dp[0][c] = True

        for i in range(1, ROWS):
            for j in range(1, COLS):
                k = i + j - 1
                if s1[i - 1] == s3[k]:
                    if dp[i - 1][j]:
                        dp[i][j] = True
                
                if s3[k] == s2[j - 1] and dp[i][j - 1]:
                    if not dp[i][j]:
                        dp[i][j] = True
        
        return dp[ROWS - 1][COLS - 1]
        
        def is_valid(i, j, k, memo):
            if k == len(s3):
                return True

            if (i, j, k) in memo:
                return memo[(i, j, k)]
            
            c1 = c2 = False
            if i < len(s1) and s3[k] == s1[i]:
                c1 = is_valid(i + 1, j, k + 1, memo)
            
            if j < len(s2) and s3[k] == s2[j]:
                c2 = is_valid(i, j + 1, k + 1, memo)
            
            memo[(i, j, k)] = c1 or c2
            return memo[(i, j, k)]
        
        return is_valid(0, 0, 0, {})
            


        