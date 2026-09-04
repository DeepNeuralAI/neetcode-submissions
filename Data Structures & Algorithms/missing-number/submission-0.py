class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] == i:
                continue
            
            correct_idx = nums[i]
            while correct_idx < n and nums[correct_idx] != correct_idx:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                correct_idx = nums[i]
        
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n