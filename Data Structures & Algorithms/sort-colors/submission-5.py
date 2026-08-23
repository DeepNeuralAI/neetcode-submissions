class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag Algorithm
        # 0 - (low - 1): 0s
        # low - (mid - 1): 1s
        # (mid - high): unsorted
        # (high + 1, n - 1): 2s

        n = len(nums)
        low = mid = 0
        high = n - 1

        while mid <= high:
            val = nums[mid]

            if val == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif val == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        



        