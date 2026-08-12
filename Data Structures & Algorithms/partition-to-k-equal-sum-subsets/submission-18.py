class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        # nums.sort(reverse = True)
        subset_target = total // k
        used = [False] * len(nums)

       
        def backtrack(start, target, k):
            if k == 0:
                return True
            
            if target == 0:
                return backtrack(0, subset_target, k - 1)
            
            if start == len(nums):
                return False
            
            for i in range(start, len(nums)):
                if used[i]: continue
        
                
                if target - nums[i] >= 0:
                    used[i] = True
                    if backtrack(i + 1, target - nums[i], k):
                        return True
                    used[i] = False
            return False
        
        return backtrack(0, subset_target, k)
            

        
                    


        