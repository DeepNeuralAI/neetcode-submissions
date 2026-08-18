class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def backtrack(i, total):
            if i == len(nums):
                return total

            exclude = backtrack(i + 1, total)  
            include = backtrack(i + 1, total ^ nums[i])

            return exclude + include
        
        return backtrack(0, 0)