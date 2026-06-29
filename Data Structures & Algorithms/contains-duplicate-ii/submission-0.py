class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        count = defaultdict(int)

        l = r = 0
       
        while r < n:
            while r - l > k:
                count[nums[l]] -= 1

                if count[nums[l]] == 0:
                    del count[nums[l]]
                
                l += 1
            
            count[nums[r]] += 1

            if count[nums[r]] > 1:
                return True
            r += 1
        return False





        