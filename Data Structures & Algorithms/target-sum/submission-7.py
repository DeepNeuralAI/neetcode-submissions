class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Bottom Up Approach
        # sum(S1) - sum(S2) = target
        # sum(S1) + sum(S2) = total
        # 2 * Sum(S1) = Total + Target
        # Sum(S1) = Total + Target // 2
        
        total = sum(nums)
        if (target + total) % 2 != 0:
            return 0
        
        # target + total must be even
        target = (target + total) // 2

        if target < 0 or target > total:
            return 0

        ROWS, COLS = len(nums), (target + 1)
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = 1
        
        if 0 < nums[0] < COLS:
            dp[0][nums[0]] = 1
        
        if nums[0] == 0:
            dp[0][0] += 1
        
        for r in range(1, ROWS):
            for c in range(COLS):
                dp[r][c] += dp[r - 1][c]

                if c - nums[r] >= 0:
                    dp[r][c] += dp[r - 1][c - nums[r]]
        
        return dp[ROWS - 1][COLS - 1]

        
        def ways(i, target, memo):
            if i == len(nums):
                if target == 0:
                    return 1
                return 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            c1 = ways(i + 1, target - nums[i], memo)
            c2 = ways(i + 1, target + nums[i], memo)
            memo[(i, target)] = c1 + c2
            return memo[(i, target)]
        
        return ways(0, target, {})


