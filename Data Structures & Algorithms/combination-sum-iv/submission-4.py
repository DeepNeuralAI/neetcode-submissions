class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Bottom Up
        nums.sort()
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, len(dp)):
            for num in nums:
                if num > i:
                    break
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]
                    
            



        