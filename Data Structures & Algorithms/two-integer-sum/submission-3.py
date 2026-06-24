class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map - Space
        n = len(nums)
        num_to_idx = {}

        for i in range(n):
            remainder = target - nums[i]
            if remainder in num_to_idx:
                return [num_to_idx[remainder], i]
            
            num_to_idx[nums[i]] = i
        
        return []