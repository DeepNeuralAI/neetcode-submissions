class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.solve(nums, 0, 0)
        
    def solve(self, nums, i, total):
        if i == len(nums):
            return total
        
        return (self.solve(nums, i + 1, total ^ nums[i]) + 
                self.solve(nums, i + 1, total))
        