class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        # Bottom Up
        
        ROWS, COLS = len(text1), len(text2)
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    c1 = dp[i][j - 1]
                    c2 = dp[i - 1][j]
                    dp[i][j] = max(c1, c2)
        
        return dp[ROWS][COLS]

        def lcs(i, j, memo):
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                return 1 + lcs(i + 1, j + 1, memo)
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            c1 = lcs(i, j + 1, memo)
            c2 = lcs(i + 1, j, memo)

            memo[(i, j)] = max(c1, c2)
            return memo[(i, j)]
        
        return lcs(0, 0, {})
    

