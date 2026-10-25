class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadene's Algorithm
        n = len(nums)
        curSum = 0
        maxSum = float('-inf')

        for i in range(n):
            if curSum < 0:
                curSum = 0
            
            curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum



