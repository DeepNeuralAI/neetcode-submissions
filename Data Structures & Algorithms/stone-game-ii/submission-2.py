class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Precompute Suffix Sum
        n = len(piles)
        suffix = [0] * n
        suffix[n - 1] = piles[n - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]
        
        def max_stones(i, M, memo):
            if i >= len(piles):
                return 0
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            best = 0
            for x in range(1, min(2 * M + 1, n - i + 1)):
                remaining = suffix[i]
                opponent = max_stones(i + x, max(M, x), memo)
                best = max(best, remaining - opponent)
            memo[(i, M)] = best 
            return memo[(i, M)]
        
        return max_stones(0, 1, {})
        
     



                
        