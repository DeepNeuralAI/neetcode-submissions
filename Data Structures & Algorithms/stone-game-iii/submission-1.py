class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def rec(i, memo):
            if i >= len(stoneValue):
                return 0
            
            if i in memo:
                return memo[i]
            
            res = float('-inf')
            for j in range(i, i + 3):
                if j < len(stoneValue):
                    res = max(
                        res,
                        sum(stoneValue[i : j + 1]) - rec(j + 1, memo)
                    )
            memo[i] = res
            return memo[i]
        
        res = rec(0, {})
        if res == 0:
            return "Tie"
        
        return "Alice" if res > 0 else "Bob"
