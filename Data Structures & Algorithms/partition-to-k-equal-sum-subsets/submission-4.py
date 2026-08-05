class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        buckets = [total_sum // k] * k
        nums.sort(reverse = True)
        return self.solve(0, nums, buckets, k)
        
    
    def solve(self, i, nums, buckets, k):
        if i == len(nums):
            return True
        
        for j in range(k):
            if j > 0 and buckets[j] == buckets[j - 1]:
                continue
            
            if buckets[j] - nums[i] >= 0:
                buckets[j] -= nums[i]
                if self.solve(i + 1, nums, buckets, k):
                    return True
                buckets[j] += nums[i]
        return False

        
        

        