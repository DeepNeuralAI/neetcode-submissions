class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Define search space
        l = max(nums)
        r = sum(nums)
        
        res = r
        while l <= r:
            m = (l + r) // 2

            if self.numSubArrays(nums, m) <= k:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
    

    def numSubArrays(self, nums, array_sum):
        res = 1
        cur_sum = 0
        
        for num in nums:
            cur_sum += num

            if cur_sum > array_sum:
                res += 1
                cur_sum = num
        
        return res
            