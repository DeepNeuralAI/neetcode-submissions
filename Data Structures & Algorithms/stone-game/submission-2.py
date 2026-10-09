class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Bottom Up
        n = len(piles)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]
        
        for l in range(n - 2, -1, -1):
            for r in range(l + 1, n):
                c1 = piles[l] - dp[l + 1][r]
                c2 = piles[r] - dp[l][r - 1]
                dp[l][r] = max(c1, c2)
        
        return dp[0][n - 1] > 0

        def solve(l, r, memo):
            if l == r:
                return piles[l]
            
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            c1 = piles[l] - solve(l + 1, r, memo)
            c2 = piles[r] - solve(l, r - 1, memo)

            memo[(l, r)] = max(c1, c2)
            return memo[(l, r)]
        
        res = solve(0, len(piles) - 1, {})
        return res > 0
        