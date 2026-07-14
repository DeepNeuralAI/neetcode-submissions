class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        
        nums.sort()
        n = len(nums)
        
        maxLen = 1
        length = 1
        
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] == (nums[i - 1] + 1):
                length += 1
            else:
                length = 1
            
            maxLen = max(maxLen, length)
        
        return maxLen