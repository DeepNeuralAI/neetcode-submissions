class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s[i] == p[j] -> dp(i + 1, j + 1)
        # p[i] == '.' -> dp(i + 1, j + 1)

        # a* - Zero occurrences -> dp(i, j + 2)
        # One or more -> dp(i + 1, j)

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
            

        