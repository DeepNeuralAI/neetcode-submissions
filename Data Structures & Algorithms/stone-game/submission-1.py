class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Memoization
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
        