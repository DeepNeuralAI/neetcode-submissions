class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Frequency Map
        n = len(nums)
        majority = n / 2
        
        cnt = 0
        candidate = None

        for i in range(n):
            if cnt == 0:
                candidate = nums[i]
                cnt = 1
            elif nums[i] == candidate:
                cnt += 1
            else:
                cnt -= 1
        
        cnt = 0
        for num in nums:
            if num == candidate:
                cnt += 1
        
        if cnt > majority:
            return candidate
        
        return -1
        