class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 1
        last = 0
        n = len(nums)

        while i < n:
            if nums[i] != nums[last]:
                last += 1
                nums[last] = nums[i]
            
            i += 1
        
        return last + 1

        