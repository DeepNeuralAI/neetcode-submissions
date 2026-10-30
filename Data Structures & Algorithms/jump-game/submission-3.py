class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Recursive - Top Down
        n = len(nums)
        
        def rec(i, cache):
            if i >= n - 1:
                return True
            
            if i in cache:
                return cache[i]
            
            for j in range(1, nums[i] + 1):
                if rec(i + j, cache):
                    cache[i] = True
                    return cache[i]
            
            cache[i] = False
            return cache[i]
        
        return rec(0, {})
            



        