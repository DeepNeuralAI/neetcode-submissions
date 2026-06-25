class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        j = n - 1
        i = 0

        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i
           
        