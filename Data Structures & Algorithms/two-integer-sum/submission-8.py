class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}

        for i in range(len(nums)):
            if target - nums[i] in num_to_idx:
                return [num_to_idx[target - nums[i]], i]
            
            num_to_idx[nums[i]] = i
        
        return []