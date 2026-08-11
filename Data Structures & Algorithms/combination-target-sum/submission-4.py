class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        current = []
        res = []

        def backtrack(i, target):
            if target == 0:
                res.append(current.copy())
                return
            
            if i == len(nums):
                return
            
            if nums[i] <= target:
                current.append(nums[i])
                backtrack(i, target - nums[i])
                current.pop()
            
            backtrack(i + 1, target)
        
        backtrack(0, target)
        return res
        