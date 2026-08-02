class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curSum = 0
        l = r = 0
        n = len(nums)
        res = float('inf')

        while r < n:
            curSum += nums[r]
            
            while curSum >= target:
                res = min(res, (r - l + 1))
                curSum -= nums[l]
                l += 1
            r += 1
        
        return 0 if res == float('inf') else res
        