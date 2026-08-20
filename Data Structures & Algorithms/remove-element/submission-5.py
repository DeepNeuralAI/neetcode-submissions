class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()

        last = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                nums[last] = nums[i]
                last += 1
        return last