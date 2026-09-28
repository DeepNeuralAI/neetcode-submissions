class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Bottom Up
        n = len(cost)
        stair_cost = [float('inf')] * (n + 1)
        stair_cost[0] = cost[0]
        
        for i in range(1, n + 1):
            stair_cost[i] = (cost[i] if i < n else 0) + min(
                stair_cost[i - 1] if i - 1 >= 0 else 0,
                stair_cost[i - 2] if i - 2 >= 0 else 0
            )

        return stair_cost[n]