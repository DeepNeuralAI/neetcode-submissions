class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Brute Force
        n = len(nums)
        majority = n / 2

        for i in range(n):
            count = 1
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1
                
            if count > majority:
                return nums[i]
        
        return -1

        