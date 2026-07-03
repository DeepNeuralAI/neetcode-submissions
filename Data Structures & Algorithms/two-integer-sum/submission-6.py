class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        modified = [(nums[i], i) for i in range(len(nums))]
        modified.sort()
        
        l = 0
        r = len(nums) - 1

        while l < r:
            candidate = modified[l][0] + modified[r][0]
            
            if candidate == target:
                return sorted([modified[l][1], modified[r][1]])
            
            if candidate < target:
                l += 1
            else:
                r -= 1
        
        return [-1, -1]
        