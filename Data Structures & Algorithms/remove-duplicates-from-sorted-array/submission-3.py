class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] != nums[last]:
                last += 1
                nums[last] = nums[i]
        
        return last + 1

        