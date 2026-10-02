class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # f(i) - length of LIS from 0..i
        # Bottom Up
        dp = [1] * len(nums)

        for i in range(1, len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)

