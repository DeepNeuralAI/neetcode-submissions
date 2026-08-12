class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        # nums.sort(reverse = True)
        subset_target = total // k
        used = [False] * len(nums)

       
        def find_subset(start, target, k):
            if target == 0:
                return backtrack(k - 1)
            
            if start == len(nums):
                return False
            
            for i in range(start, len(nums)):
                if used[i]: continue
                
                
                if target - nums[i] >= 0:
                    used[i] = True
                    if find_subset(i + 1, target - nums[i], k):
                        return True
                    used[i] = False
            return False

        def backtrack(k):
            if k == 0:
                return True
    
            return find_subset(0, subset_target, k)
        
        return backtrack(k)
            

        
                    


        