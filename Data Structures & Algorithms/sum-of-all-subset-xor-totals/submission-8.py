class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.subset_sum = 0
        curr = 0

        def backtrack(i, curr):
            if i == len(nums):
                return curr
            
            return backtrack(i + 1, curr ^ nums[i]) + backtrack(i + 1, curr)
        
        return backtrack(0, curr)

            

        