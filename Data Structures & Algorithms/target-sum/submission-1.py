class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def ways(i, target, memo):
            if i == len(nums):
                if target == 0:
                    return 1
                return 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            c1 = ways(i + 1, target - nums[i], memo)
            c2 = ways(i + 1, target + nums[i], memo)
            memo[(i, target)] = c1 + c2
            return memo[(i, target)]
        
        return ways(0, target, {})


