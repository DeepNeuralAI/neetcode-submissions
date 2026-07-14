class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        maxLen = 0

        for num in nums:
            seen.add(num)
        
        for num in nums:
            if num - 1 in seen:
                continue
            
            length  = 1
            while num + 1 in seen:
                length += 1
                num = num + 1
            
            maxLen = max(maxLen, length)
        
        return maxLen
        