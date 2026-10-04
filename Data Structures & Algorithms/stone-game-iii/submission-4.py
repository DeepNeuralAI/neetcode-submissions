class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Bottom Up
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            take = 0
            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                dp[i] = max(
                    dp[i],
                    take - dp[j + 1]
                )
        
        res = dp[0]
        if res == 0:
            return "Tie"
        
        return "Alice" if res > 0 else "Bob"

        def rec(i, memo):
            if i >= len(stoneValue):
                return 0
            
            if i in memo:
                return memo[i]
            
            res = float('-inf')
            take = 0
            for j in range(i, min((i + 3), len(stoneValue))):
                take += stoneValue[j]
                res = max(
                    res,
                    take - rec(j + 1, memo)
                )
            memo[i] = res
            return memo[i]
        
        res = rec(0, {})
        if res == 0:
            return "Tie"
        
        return "Alice" if res > 0 else "Bob"
