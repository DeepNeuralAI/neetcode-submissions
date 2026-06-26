class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Using Sorting
        nums.sort()
        n = len(nums)
        ans = []

        i = j = 0
        while i < n:
            while j < n and nums[j] == nums[i]:
                j += 1
            
            length = (j - i)
            if length > n / 3:
                ans.append(nums[i])
            
            i = j
        return ans
