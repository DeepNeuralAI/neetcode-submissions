class Solution:
    def rob(self, nums: List[int]) -> int:
        # Bottom Up Approach
        if not nums:
            return 0
        
        if len(nums) == 1:
            return max(0, nums[0])

        profit = [0] * len(nums)
        profit[0] = nums[0]
        profit[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            profit[i] = max(
                nums[i] + profit[i - 2],
                profit[i - 1]
            )
        
        return profit[len(nums) - 1]



