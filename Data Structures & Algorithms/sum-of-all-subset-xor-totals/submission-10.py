class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        self.total = 0
        
        def backtrack(i, xor):
            self.total += xor

            for j in range(i, len(nums)):
                xor ^= nums[j]
                backtrack(j + 1, xor)
                xor ^= nums[j]
        
        backtrack(0, 0)
        return self.total

            

        