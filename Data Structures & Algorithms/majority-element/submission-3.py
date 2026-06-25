class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore
        n = len(nums)
        majority = n / 2

        cnt = 1
        candidate = nums[0]

        for i in range(1, n):
            if nums[i] == candidate:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt < 0:
                candidate = nums[i]
                cnt = 1
        
        cnt = 0
        for i in range(n):
            if nums[i] == candidate:
                cnt += 1
            
        if cnt > majority:
            return candidate
        
        return -1


        