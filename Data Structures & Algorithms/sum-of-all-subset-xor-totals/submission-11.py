class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
    
        def backtrack(i, xor):
            if i == len(nums):
                return xor
            
            return backtrack(i + 1, nums[i] ^ xor) + backtrack(i + 1, xor)
        
        return backtrack(0, 0)
         
            

        