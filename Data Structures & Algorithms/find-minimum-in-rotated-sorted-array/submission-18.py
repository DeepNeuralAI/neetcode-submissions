class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        r = n - 1
        res = float('inf')

        while l <= r:
            m = (l + r) // 2

            if nums[m] <= nums[r]:
                res = min(res, nums[m])
                r = m - 1
            else:
                l = m + 1
        return res

        