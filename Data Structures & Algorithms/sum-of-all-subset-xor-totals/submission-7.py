class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.subset_sum = 0
        curr = 0

        def backtrack(i, curr):
            if i == len(nums):
                self.subset_sum += curr
                return
            
            curr ^= nums[i]
            backtrack(i + 1, curr)
            curr ^= nums[i]
            backtrack(i + 1, curr)
        
        backtrack(0, curr)
        return self.subset_sum

            

        