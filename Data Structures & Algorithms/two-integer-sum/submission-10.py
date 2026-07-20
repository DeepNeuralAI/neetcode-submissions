class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = [(num, i) for i, num in enumerate(nums)]
        sorted_nums.sort()
        n = len(nums)

        i = 0
        j = n - 1
        while i < j:
            candidate = sorted_nums[i][0] + sorted_nums[j][0]
            if candidate == target:
                ans = [sorted_nums[i][1], sorted_nums[j][1]]
                return sorted(ans)
            
            if candidate < target:
                i += 1
            else:
                j -= 1
        
        return [-1, -1]
        