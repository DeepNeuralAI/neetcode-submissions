class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        # Optimal
        def backtrack(i, curr, target):
            if target == 0:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                if nums[j] > target:
                    return

                curr.append(nums[j])
                backtrack(j, curr, target - nums[j])
                curr.pop()
        
        res = []
        backtrack(0, [], target)
        return res
        