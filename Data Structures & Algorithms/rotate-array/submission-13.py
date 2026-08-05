class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        nums=[1,2,3,4,5,6,7]
        k = 3
        nums = [0 1 2 1 2 3 6]
        temp = [5, 6, 7]

        """
        temp = []
        n = len(nums)
        k = k % n
        temp = []
        
        for i in range(n - k, n):
            temp.append(nums[i])
        
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]
        
        for i in range(k):
            nums[i] = temp[i]
