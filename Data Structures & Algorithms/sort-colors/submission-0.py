class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Brute Force
        cnt0 = cnt1 = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 0:
                cnt0 += 1
            elif nums[i] == 1:
                cnt1 += 1
        
        for i in range(cnt0):
            nums[i] = 0
        
        k = cnt0 + cnt1
        for i in range(cnt0, k):
            nums[i] = 1
        
        for i in range(k, n):
            nums[i] = 2
