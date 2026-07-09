class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        i = j = 0
        seen = set()

        while j < n:
            while j - i > k:
                seen.remove(nums[i])
                i += 1
            
            if nums[j] in seen:
                return True
        
            seen.add(nums[j])
            
            
            j += 1
        return False
            

        