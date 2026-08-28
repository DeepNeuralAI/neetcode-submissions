class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        maxLen = 0

        for i in range(len(nums)):
            num = nums[i]
            if num - 1 in seen:
                continue
            
            length = 1
            while num + 1 in seen:
                length += 1
                num = num + 1
            
            maxLen = max(length, maxLen)
        
        return maxLen
        