class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map - One Pass
        seen = {}
        n = len(nums)

        for i in range(n):
            need = target - nums[i]

            if need in seen:
                return [seen[need], i]
            
            seen[nums[i]] = i
        
        return []