class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = 0
        def backtrack(i, xor):
            if i == len(nums):
                return xor
            
            return backtrack(i + 1, xor ^ nums[i]) + backtrack(i + 1, xor)
        
        return backtrack(0, xor)
        

        