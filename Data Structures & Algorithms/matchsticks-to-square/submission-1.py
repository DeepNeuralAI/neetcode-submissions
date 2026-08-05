class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # 2l + 2w = sum of lengths
        # l = w
        # 4w = sum of lengths
        # If sum of lengths not divisible by 4 -- return false

        if not matchsticks:
            return True
        
        if sum(matchsticks) % 4 != 0:
            return False
        
        matchsticks.sort(reverse = True)
        
        buckets = [sum(matchsticks) // 4] * 4
        return self.solve(0, buckets, matchsticks)
    
    def solve(self, i, buckets, nums):
        if i == len(nums):
            for b in buckets:
                if b != 0:
                    return False
            return True
        
        for k in range(len(buckets)):
            if buckets[k] - nums[i] >= 0:
                buckets[k] -= nums[i]
                if self.solve(i + 1, buckets, nums):
                    return True
                buckets[k] += nums[i]
        return False
