class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Prefix Product & Suffix Product
        prefix = suffix = 1
        res = float('-inf')
        
        for i in range(len(nums)):
            j = len(nums) - i - 1
            prefix *= nums[i]
            suffix *= nums[j]

            res = max(res, prefix, suffix)

            if prefix == 0:
                prefix = 1
            
            if suffix == 0:
                suffix = 1
        
        return res
            



            

        




        