class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        
        def backtrack(i, current, target):
            if target == 0:
                res.append(current.copy())
                return
            
            if i == len(nums):
                return
            
            for j in range(i, len(nums)):
                if target - nums[j] >= 0:
                    current.append(nums[j])
                    backtrack(j, current, target - nums[j])
                    current.pop()
        
        res = []
        backtrack(0, [], target)
        return res
        