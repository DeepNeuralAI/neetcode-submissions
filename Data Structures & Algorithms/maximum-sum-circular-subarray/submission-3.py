class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        min_dp = [0] * n
        max_dp = [0] * n
        
        min_dp[0] = nums[0]
        max_dp[0] = nums[0]

        global_min = global_max = nums[0]

        for i in range(1, n):
            max_dp[i] = max(
                nums[i] + max_dp[i - 1],
                nums[i]
            )

            min_dp[i] = min(
                nums[i] + min_dp[i - 1],
                nums[i]
            )

            global_min = min(global_min, min_dp[i])
            global_max = max(global_max, max_dp[i])
        
       
        
        total_sum = sum(nums)
        circular_max = total_sum - global_min

        if total_sum == global_min:
            return global_max
        
        return max(global_max, circular_max)




    
        