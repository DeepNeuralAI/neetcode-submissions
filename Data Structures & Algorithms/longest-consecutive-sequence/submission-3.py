class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums:
            seen.add(num)
        
        maxLen = 0
        for num in nums:
            if (num - 1) in seen:
                continue
            
            length = 1
            curr = num + 1
            
            while curr in seen:
                curr = curr + 1
                length += 1
            
            maxLen = max(maxLen, length)
        
        return maxLen
        