class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2
            val = nums[m] 
            if val == target:
                return m
            
            if val < target:
                l = m + 1
            else:
                r = m
        return l