class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = 0

        for num in nums:
            if num != val:
                nums[last] = num
                last += 1
        
        return last
        