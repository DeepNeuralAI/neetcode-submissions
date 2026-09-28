class Solution:
    def climbStairs(self, n: int) -> int:
        # Top Down
        memo = {}
        def num_ways(i):
            if i == n:
                return 1
            
            if i > n:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = num_ways(i + 1) + num_ways(i + 2)
            return memo[i]
        
        return num_ways(0)