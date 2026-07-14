class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = j = 0
        n = len(nums)
        seen = set()

        while j < n:
            if j - i > k:
                seen.remove(nums[i])
                i += 1
            
            if nums[j] in seen:
                return True
            
            seen.add(nums[j])

            j += 1
        return False


        