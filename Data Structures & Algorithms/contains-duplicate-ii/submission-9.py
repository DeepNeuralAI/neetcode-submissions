class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, min(n, i + k + 1)):
                if nums[i] == nums[j]:
                    return True
        return False


