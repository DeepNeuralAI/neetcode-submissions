class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom Up
        n = len(cost)
        stair_cost = [float('inf')] * (n + 1)
        stair_cost[n] = 0

        for i in range(n - 1, -1, -1):
            stair_cost[i] = cost[i] + min(
                stair_cost[i + 1] if i + 1 <= n else 0,
                stair_cost[i + 2] if i + 2 <= n else 0
            )
        
        return min(stair_cost[0], stair_cost[1])