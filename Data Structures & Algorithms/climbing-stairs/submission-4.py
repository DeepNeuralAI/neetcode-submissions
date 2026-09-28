class Solution:
    def climbStairs(self, n: int) -> int:
        # Space Optimized
        prev = 1
        before_prev = 0

        for i in range(1, n + 1):
            ways = prev + before_prev
            before_prev = prev
            prev = ways
        
        return prev
