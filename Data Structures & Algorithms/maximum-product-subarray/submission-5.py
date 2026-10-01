class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Dynamic Programming - Kadane's Algorithm
        n = len(nums)

        if n == 1:
            return nums[0]
            
        max_dp = [0] * n
        min_dp = [0] * n

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        res = float('-inf')

        for i in range(1, n):
            x = nums[i]
            max_dp[i] = max(
                x, 
                min_dp[i - 1] * x,
                max_dp[i - 1] * x
            )

            min_dp[i] = min(
                x, 
                min_dp[i - 1] * x,
                max_dp[i - 1] * x
            )

            res = max(res, min_dp[i], max_dp[i])
        
        return res if res != float('-inf') else -1








            

        




        