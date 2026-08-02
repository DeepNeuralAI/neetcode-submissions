class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = r = 0
        n = len(nums)
        mp = defaultdict(int)

        for i in range(n):
            if nums[i] in mp and abs(mp[nums[i]] - i) <= k:
                return True
            mp[nums[i]] = i
        
        return False
