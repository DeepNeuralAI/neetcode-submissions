class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
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
    

