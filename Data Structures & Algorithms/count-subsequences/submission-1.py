class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def num_ways(i, j, memo):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i < len(s) and j < len(t) and s[i] != t[j]:
                return num_ways(i + 1, j, memo)
            
            c1 = 0
            if i < len(s) and j < len(t) and s[i] == t[j]:
                c1 = num_ways(i + 1, j + 1, memo)
            
            c2 = num_ways(i + 1, j, memo)
            memo[(i, j)] =  c1 + c2
            return memo[(i, j)]
        
        return num_ways(0, 0, {})
        



        