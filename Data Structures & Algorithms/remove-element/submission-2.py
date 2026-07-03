class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        last = 0

        for i in range(n):
            if nums[i] != val:
                nums[last] = nums[i]
                last += 1
        
        return last
        