class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
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
            


        