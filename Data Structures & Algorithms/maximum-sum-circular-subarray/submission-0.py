class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        
        maxSum = curMax = nums[0]
        minSum = curMin = nums[0]
        total = nums[0]
        
        for i in range(1, n):
            total += nums[i]
            curMax = max(curMax + nums[i], nums[i])
            curMin = min(curMin + nums[i], nums[i])
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)

        if total == minSum:
            return maxSum
        
        return max(total - minSum, maxSum)

        