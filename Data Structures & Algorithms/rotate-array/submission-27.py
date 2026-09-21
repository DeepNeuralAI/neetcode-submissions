class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        n = len(nums)

        def rotate(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        rotate(nums, 0, n - k - 1)
        rotate(nums, n - k, n - 1)
        rotate(nums, 0, n - 1)
        
        
        

