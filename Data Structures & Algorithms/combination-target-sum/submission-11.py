class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Optimal
        def backtrack(i, curr, target):
            if target == 0:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                if target >= nums[j]:
                    curr.append(nums[j])
                    backtrack(j, curr, target - nums[j])
                    curr.pop()
        
        res = []
        backtrack(0, [], target)
        return res
        