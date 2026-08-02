class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.solve(nums, 0, 0)

    def solve(self, nums, i, cur_xor):
        if i == len(nums):
            return cur_xor
        
        return (self.solve(nums, i + 1, cur_xor ^ nums[i]) + 
        self.solve(nums, i + 1, cur_xor))
        