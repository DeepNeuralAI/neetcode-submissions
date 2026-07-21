class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = curSum = 0
        n = len(nums)
        minLen = float('inf')


        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                if curSum >= target:
                    minLen = min(minLen, j - i + 1)
                    break

        
        return 0 if minLen == float('inf') else minLen

        