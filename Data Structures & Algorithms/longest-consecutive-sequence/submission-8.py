class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLen = 0

        for num in nums:
            if num - 1 in seen:
                continue
            
            length = 1
            while num + 1 in seen:
                length += 1
                num = num + 1
            
            maxLen = max(length, maxLen)
        
        return maxLen
