class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = set()
        
        for r in range(min(k + 1, n)):
            if nums[r] in seen:
                return True
            seen.add(nums[r])

        l = 0
        for i in range(k + 1, n):
            seen.remove(nums[l])
            l += 1

            if nums[i] in seen:
                return True

            seen.add(nums[i])
        
        return False