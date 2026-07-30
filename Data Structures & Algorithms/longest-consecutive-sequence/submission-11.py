class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
       
        n = len(nums)
        maxLen = 0
        length = 0
        
        for i in range(n):
            num = nums[i]
            length = 1
            while num + 1 in nums:
                length += 1
                num += 1
            maxLen = max(maxLen, length)
        return maxLen
                
           
                



