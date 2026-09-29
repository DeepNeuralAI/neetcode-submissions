class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.recursive(nums, 0, {})

    def recursive(self, nums, i, memo):
        if i >= len(nums):
            return 0
        
        if i in memo:
            return memo[i]
        
        memo[i] = max(
            nums[i] + self.recursive(nums, i + 2, memo),
            self.recursive(nums, i + 1, memo)
        )

        return memo[i]

