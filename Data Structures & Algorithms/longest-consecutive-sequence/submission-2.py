class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        n = len(nums)

        length = 1
        maxLen = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            
            if nums[i] == nums[i - 1] + 1:
                length += 1
            else:
                length = 1
            maxLen = max(length, maxLen)
        
        return maxLen

