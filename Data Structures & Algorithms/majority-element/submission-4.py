class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore
        cnt = 0
        candidate = nums[0]
        n = len(nums)

        for i in range(n):
            if cnt == 0:
                candidate = nums[i]
                cnt += 1
            elif candidate == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        
        cnt = 0
        expected = n / 2
        for num in nums:
            if num == candidate:
                cnt += 1
        
        return candidate if cnt > expected else -1
        