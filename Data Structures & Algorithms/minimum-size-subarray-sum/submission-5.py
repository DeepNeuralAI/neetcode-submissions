class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = curSum = 0
        n = len(nums)
        minLen = float('inf')


        while r < n:
            curSum += nums[r]

            while curSum >= target:
                minLen = min(minLen, r - l + 1)
                curSum -= nums[l]
                l += 1
            
            r += 1
        
        return 0 if minLen == float('inf') else minLen

        