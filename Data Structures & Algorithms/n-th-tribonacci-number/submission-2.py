class Solution:
    def tribonacci(self, n: int) -> int:
        # Memoization
        def trib(n, memo):
            if n == 0:
                return 0
            
            if n in (1, 2):
                return 1
            
            if n in memo:
                return memo[n]
            
            memo[n] = trib(n - 1, memo) + trib(n - 2, memo) + trib(n - 3, memo)
            return memo[n]
        
        return trib(n, {})
        