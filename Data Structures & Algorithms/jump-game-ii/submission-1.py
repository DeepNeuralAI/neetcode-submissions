class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # Bottom Up
        dp = [float('inf')] * n
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                continue
            
            endIndex = min(i + nums[i], n - 1)
            for j in range(i + 1, endIndex + 1):
                dp[i] = min(
                    1 + dp[j],
                    dp[i]
                )
   
        return dp[0]
        
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
                
                

        