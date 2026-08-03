class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, i, current, res):
        if i == len(nums):
            res.append(current.copy())
            return
        
        current.append(nums[i])
        self.dfs(nums, i + 1, current, res)
        current.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        
        self.dfs(nums, i + 1, current, res)

        