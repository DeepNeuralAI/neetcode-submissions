class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums = self.bubble(nums)
        return nums



    def bubble(self, nums):
        n = len(nums)

        for i in range(n - 1):
            j = n - i - 1
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
            
        return nums
