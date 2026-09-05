class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Sliding Window
        l = r = 0
        seen = set()
        n = len(nums)

        while r < n:
            if (r - l) > k:
                seen.remove(nums[l])
                l += 1
            
            if nums[r] in seen:
                return True
            
            seen.add(nums[r])
            r += 1
        
        return False

        