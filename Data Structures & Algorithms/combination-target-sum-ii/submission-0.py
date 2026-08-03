class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(0, target, candidates, [], res)
        return res


    def dfs(self, i, target, nums, current, res):
        if target == 0:
            res.append(current.copy())
            return
        
        if target < 0 or i == len(nums):
            return

        
        current.append(nums[i])
        self.dfs(i + 1, target - nums[i], nums, current, res)
        current.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.dfs(i + 1, target, nums, current, res)