class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_needed = n / 2

        cnt = 0
        candidate = None

        for i in range(n):
            if cnt == 0:
                candidate = nums[i]
                cnt += 1
            elif nums[i] == candidate:
                cnt += 1
            else:
                cnt -= 1
    
        return candidate

        