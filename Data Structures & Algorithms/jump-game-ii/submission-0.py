class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        def rec(i, cache):
            if i >= n - 1:
                return 0
            
            if i in cache:
                return cache[i]

            minJumps = n
            for j in range(1, nums[i] + 1):
                jumps = 1 + rec(i + j, cache)
                minJumps = min(minJumps, jumps)

            cache[i] = minJumps
            return cache[i]
        
        return rec(0, {})
                
                

        