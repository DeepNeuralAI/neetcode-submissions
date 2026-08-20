class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        sorted_nums = [(nums[i], i) for i in range(n)]
        sorted_nums.sort()

        l = 0
        r = n - 1

        while l < r:
            candidate = sorted_nums[l][0] + sorted_nums[r][0]
            if candidate == target:
                ans = [sorted_nums[l][1], sorted_nums[r][1]]
                return sorted(ans)
            
            if candidate < target:
                l += 1
            else:
                r -= 1
        
        return [-1, -1]
        