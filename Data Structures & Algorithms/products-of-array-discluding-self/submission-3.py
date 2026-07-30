class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProduct = [1] * n
        suffixProduct = [1] * n

        prefixProduct[0] = nums[0]
        suffixProduct[n - 1] = nums[n - 1]

        j = n - 2
        for i in range(1, n):
            prefixProduct[i] = nums[i] * prefixProduct[i - 1]
            suffixProduct[j] = nums[j] * suffixProduct[j + 1]
            j -= 1
        
        res = [0] * n
        for i in range(n):
            prefix = prefixProduct[i - 1] if i > 0 else 1
            suffix = suffixProduct[i + 1] if i < n - 1 else 1
            res[i] = prefix * suffix
        
        return res


        