class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = 0
        n = len(nums)
        minLen = len(nums) + 1

        l = r = 0

        while r < n:
            curSum += nums[r]

            while curSum >= target:
                minLen = min(r - l + 1, minLen)
                curSum -= nums[l]
                l += 1
            
            r += 1
        
        if minLen > n:
            return 0
        
        return minLen