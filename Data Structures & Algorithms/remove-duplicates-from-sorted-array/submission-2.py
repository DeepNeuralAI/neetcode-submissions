class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[last - 1]:
                nums[last] = nums[i]
                last += 1
        
        return last
        