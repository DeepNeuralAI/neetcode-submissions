class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadene's Algorithm
        n = len(nums)
        curSum = 0
        maxSum = float('-inf')

        for i in range(n):
            curSum = max(curSum + nums[i], nums[i])
            maxSum = max(maxSum, curSum)
        
        return maxSum



