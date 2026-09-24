class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def backtrack(i, curr, target):
            if target == 0:
                res.append(curr.copy())
                return
            
            if i == len(nums) or target < 0:
                return
            
            if target >= nums[i]:
                curr.append(nums[i])
                backtrack(i, curr, target - nums[i])
                curr.pop()
            
            backtrack(i + 1, curr, target)
        
        res = []
        backtrack(0, [], target)
        return res
        