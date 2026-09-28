class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        self.total = 0
    
        def backtrack(i, xor):
            

            if i == len(nums):
                self.total += xor
                return
            
            xor ^= nums[i]
            backtrack(i + 1, xor)
            xor ^= nums[i]
            backtrack(i + 1, xor)
        
        backtrack(0, 0)
        return self.total
        
         
            

        