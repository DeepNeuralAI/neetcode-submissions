class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = last = 1
        n = len(nums)

        while i < n:
            if nums[i] != nums[i - 1]:
                nums[last] = nums[i]
                last += 1
            
            i += 1
        
        return last

        