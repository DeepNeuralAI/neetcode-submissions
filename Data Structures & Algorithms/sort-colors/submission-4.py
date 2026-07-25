class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag Algorithm
        # 0 to low - 1: 0s
        # low to mid - 1: 1s
        # high + 1 to n - 1: 2s

        low = mid = 0
        high = len(nums) - 1

        # 0 0 0 0 0 1 1 1 1 x 1 2 2 2


        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        return nums