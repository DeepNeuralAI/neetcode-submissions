class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, 0, res, [])
        return res
    
    def backtrack(self, nums, i, res, curPath):
        if i == len(nums):
            res.append(curPath.copy())
            return
        
        curPath.append(nums[i])
        self.backtrack(nums, i + 1, res, curPath)
        curPath.pop()

        self.backtrack(nums, i + 1, res, curPath)
        