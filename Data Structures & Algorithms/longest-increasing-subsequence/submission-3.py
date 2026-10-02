class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # f(i) - length of LIS from 0..i
        # Memoized
        def lis(i, prev_max = float('-inf'), memo = {}):
            if i == len(nums):
                return 0
            
            if (i, prev_max) in memo:
                return memo[(i, prev_max)]
            
            take = 0
            if nums[i] > prev_max:
                take = 1 + lis(i + 1, nums[i], memo)
            skip = lis(i + 1, prev_max, memo)
            memo[(i, prev_max)] = max(take, skip)
            return memo[(i, prev_max)]

        return lis(0)