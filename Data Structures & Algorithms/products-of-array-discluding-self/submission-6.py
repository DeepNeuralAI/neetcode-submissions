class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [1] * n
        suffixProduct = [1] * n

        for i in range(1, n):
            prefixProduct[i] = nums[i - 1] * prefixProduct[i - 1]
            suffixProduct[n - i - 1] = nums[n - i] * suffixProduct[n - i]
        
        res = [0] * n
        for i in range(n):
            prefix = prefixProduct[i]
            suffix = suffixProduct[i]
            res[i] = prefix * suffix
        
        return res


        