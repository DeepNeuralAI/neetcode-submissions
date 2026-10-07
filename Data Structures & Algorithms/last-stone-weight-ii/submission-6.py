class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Modify to Subset Sum Target
        total_sum = sum(stones)
        target = (total_sum // 2)

        ROWS, COLS = len(stones), (target + 1)
        dp = [[False] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            dp[r][0] = True

        if stones[0] < COLS:
            dp[0][stones[0]] = True
        
        for i in range(1, ROWS):
            for target in range(1, COLS):
                dp[i][target] = dp[i - 1][target]

                if target - stones[i] >= 0:
                    dp[i][target] = dp[i][target] or dp[i - 1][target - stones[i]]
        
        for target in range(COLS - 1, -1, -1):
            if dp[ROWS - 1][target]:
                return abs(total_sum - target - target)
        
        return -1




        