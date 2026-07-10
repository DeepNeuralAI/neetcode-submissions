class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            candidate = nums[m]
            if candidate == target:
                return m
            
            if candidate < target:
                l = m + 1
            else:
                r = m - 1
        
        return l