class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Memo
        n = len(cost)
        memo = {}
        
        def min_cost(i, cost, memo):
            n = len(cost)

            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(
                min_cost(i + 1, cost, memo),
                min_cost(i + 2, cost, memo)
            )
            return memo[i]
        
        return min(min_cost(0, cost, memo), min_cost(1, cost, memo))
            


        