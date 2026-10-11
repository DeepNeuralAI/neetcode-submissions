class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s[i] == p[j] -> dp(i + 1, j + 1)
        # p[i] == '.' -> dp(i + 1, j + 1)

        # a* - Zero occurrences -> dp(i, j + 2)
        # One or more -> dp(i + 1, j)

        # Bottom Up Approach\
        if not p:
            return not s
        
        ROWS, COLS = len(s) + 1, len(p) + 1
        dp = [[False] * COLS for _ in range(ROWS)]
        dp[0][0] = True


        for c in range(2, COLS):
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                s_char = s[r - 1]
                p_char = p[c - 1]

                if p_char == '*':
                    # Zero Occurrences
                    dp[r][c] = dp[r][c - 2]

                    prev_char = p[c - 2]
                    if prev_char == '.' or prev_char == s_char:
                        dp[r][c] = dp[r][c] or dp[r - 1][c]
                else:
                    if p_char == '.' or p_char == s_char:
                        dp[r][c] = dp[r - 1][c - 1]
                
              
        
        return dp[ROWS - 1][COLS - 1]


        
            
        def is_valid(i, j, memo):
            if j == len(p):
                return i == len(s)
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            match = False
            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                match = True
            
            if j + 1 < len(p) and p[j + 1] == '*':
                # Zero occurrence
                c1 = is_valid(i, j + 2, memo)

                c2 = False
                if match:
                    c2 = is_valid(i + 1, j, memo)
                
                memo[(i, j)] = c1 or c2
                return memo[(i, j)]
            elif match:
                memo[(i, j)] = is_valid(i + 1, j + 1, memo)
                return memo[(i, j)]
            
            memo[(i, j)] = False
            return memo[(i, j)]
            
        
        return is_valid(0, 0, {})
            

        