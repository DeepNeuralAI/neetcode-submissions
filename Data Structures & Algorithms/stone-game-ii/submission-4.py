class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Precompute Suffix Sum
        n = len(piles)
        suffix = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                best = 0
                max_M = min(2 * M, n - i)

                for X in range(1, max_M+ 1):
                    new_M = max(X, M)
                    best = max(
                        best,
                        suffix[i] - dp[i + X][new_M]
                    )
                dp[i][M] = best
    
        return dp[0][1]
                        


     



                
        