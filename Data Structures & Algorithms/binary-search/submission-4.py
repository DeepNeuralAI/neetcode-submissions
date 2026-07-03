class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n

        while l < r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if l < n and nums[l] == target else -1

        