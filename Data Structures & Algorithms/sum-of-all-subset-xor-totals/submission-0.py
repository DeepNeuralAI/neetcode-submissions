class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        self.solve(nums, 0, 0, res)
        
        return sum(res)

    def solve(self, nums, i, cur_xor, res):
        if i == len(nums):
            res.append(cur_xor)
            return
        
        self.solve(nums, i + 1, cur_xor ^ nums[i], res)
        self.solve(nums, i + 1, cur_xor, res)
        