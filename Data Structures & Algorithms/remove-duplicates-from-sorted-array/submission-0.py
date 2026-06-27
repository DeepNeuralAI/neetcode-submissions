class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        last = 0
        j = 1

        while j < n:
            if nums[j] != nums[last]:
                last += 1
                nums[last] = nums[j]
            
            j += 1
        
        return last + 1

        