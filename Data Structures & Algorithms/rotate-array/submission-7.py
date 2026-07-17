class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        tmp = []
        for i in range(n - k, n):
            tmp.append(nums[i])
        
        for i in range(n - 1, -1, -1):
            if i - k >= 0:
                nums[i] = nums[i - k]
            
        for i in range(k):
            nums[i] = tmp[i]
    
        