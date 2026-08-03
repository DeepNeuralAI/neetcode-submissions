class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.solve(nums, 0, target, [], res)
        return res


    def solve(self, nums, i, target, current_path, res):
        if target == 0:
            res.append(current_path.copy())
            return
        
        if i == len(nums) or target < 0:
            return
        
        
        current_path.append(nums[i])
        include = self.solve(nums, i, target - nums[i], current_path, res)
        current_path.pop()
        
        exclude = self.solve(nums, i + 1, target, current_path, res)
        
        return include or exclude