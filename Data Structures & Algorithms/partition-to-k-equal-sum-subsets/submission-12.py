class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        
        if total_sum % k != 0:
            return False
        
        target = total_sum // k
        used = [False] * len(nums)
        
        nums.sort(reverse = True)
        
        
        def backtrack(i, k, subset_sum):
            if k == 0:
                return True
            
            if subset_sum == target:
                return backtrack(0, k - 1, 0)
            
            if i == len(nums):
                return False

            for j in range(i, len(nums)):
                if used[j] or subset_sum + nums[j] > target:
                    continue
                
                used[j] = True
                
                if backtrack(j, k, subset_sum + nums[j]):
                    return True
                
                used[j] = False
            
            return False

        return backtrack(0, k, 0)
        
   

        