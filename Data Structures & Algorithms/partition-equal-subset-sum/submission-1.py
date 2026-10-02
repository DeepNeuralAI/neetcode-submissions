class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Memoization
        # Find a subset that equals sum(nums) // 2

        if sum(nums) % 2 != 0:
            return False

        def subset(i, target, memo):
            if target == 0:
                return True
            
            if i == len(nums):
                return False
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            c1 = False
            if target - nums[i] >= 0:
                c1 = subset(i + 1, target - nums[i], memo)
            
            c2 = subset(i + 1, target, memo)
            memo[(i, target)] = c1 or c2
            return memo[(i, target)] 
             
        
        return subset(0, sum(nums) // 2, {})
            
        