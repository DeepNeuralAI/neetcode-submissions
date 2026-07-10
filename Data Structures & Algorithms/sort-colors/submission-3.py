class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag Algorithm
        # 0: 0 to low - 1
        # 1: low to mid - 1
        # unsorted: mid to high
        # 2: high + 1 to n - 1

        # 0 0 0 0 0 1 1 1 x x x 2 2 2 2
        n = len(nums)
        low = mid = 0
        high = n - 1

        while mid <= high:
            value = nums[mid]
            if value == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif value == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        

            
