class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        def backtrack(i, xor):
            if i == len(nums):
                return xor
            
            include = backtrack(i + 1, xor ^ nums[i])
            exclude = backtrack(i + 1, xor)

            return include + exclude
        
        return backtrack(0, 0)

        