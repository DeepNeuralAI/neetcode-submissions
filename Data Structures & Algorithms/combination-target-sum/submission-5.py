class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        current = []
        res = []

        def backtrack(i, target):
            if target == 0:
                res.append(current.copy())
                return
            
            for start in range(i, len(nums)):
                if nums[start] <= target:
                    current.append(nums[start])
                    backtrack(start, target - nums[start])
                    current.pop()
            
        backtrack(0, target)
        return res
        