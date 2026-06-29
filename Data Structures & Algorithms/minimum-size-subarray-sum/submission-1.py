class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        curSum = 0
        res = n + 1
        
        while r < n:
            curSum += nums[r]

            while curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1
            
            r += 1
        
        return 0 if res == (n + 1) else res



        