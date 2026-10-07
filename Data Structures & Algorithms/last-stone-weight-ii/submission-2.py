class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        def dfs(i, subset1, subset2, memo):
            if i == len(stones):
                return abs(subset1 - subset2)
            
            if (i, subset1, subset2) in memo:
                return memo[((i, subset1, subset2))]
            
            c1 = dfs(i + 1, stones[i] + subset1, subset2, memo)
            c2 = dfs(i + 1, subset1, subset2 + stones[i], memo)
            memo[((i, subset1, subset2))] = min(c1, c2)

            return memo[((i, subset1, subset2))]
        
        return dfs(0, 0, 0, {})
        