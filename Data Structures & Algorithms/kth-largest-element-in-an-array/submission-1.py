class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Brute Force
        nums.sort()
        n = len(nums)
        return nums[n - k]

        