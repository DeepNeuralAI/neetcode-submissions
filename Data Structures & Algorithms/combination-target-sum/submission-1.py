class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        def backtrack(i, current, target):
            if target == 0:
                res.append(current.copy())
                return
            
            if i == len(nums):
                return
            
            if target - nums[i] >= 0:
                current.append(nums[i])
                backtrack(i, current, target - nums[i])
                current.pop()
            
            backtrack(i + 1, current, target)
        
        res = []
        backtrack(0, [], target)
        return res
        