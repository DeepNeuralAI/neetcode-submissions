class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        nums.sort(reverse = True)
        buckets = [total // k] * k
        
        def backtrack(i):
            if i == len(nums):
                return True
            
            for j in range(len(buckets)):
                if j > 0 and buckets[j] == buckets[j - 1]:
                    continue
                    
                if buckets[j] >= nums[i]:
                    buckets[j] -= nums[i]
                    
                    if backtrack(i + 1):
                        return True
                    
                    buckets[j] += nums[i]
            return False
        
        return backtrack(0)
        
                    


        