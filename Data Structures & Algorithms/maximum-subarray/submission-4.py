class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Bottom Up
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        global_max = nums[0]

        for i in range(1, n):
            dp[i] = max(
                dp[i - 1] + nums[i],
                nums[i]
            )
            global_max = max(global_max, dp[i])
        
        return global_max


