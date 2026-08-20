class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        num_to_idx_map = {}

        for i in range(n):
            need = target - nums[i]
            if need in num_to_idx_map:
                return [num_to_idx_map[need], i]
        
            num_to_idx_map[nums[i]] = i
        
        return [-1, -1]
        