class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Negative Marking
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                return abs(nums[i])
            
            nums[idx] *= -1
        
        return len(nums)




        