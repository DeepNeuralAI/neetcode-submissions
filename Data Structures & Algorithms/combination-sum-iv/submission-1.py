class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def ways(n, memo):
            if n == 0:
                return 1
            
            if n < 0:
                return 0
            
            if n in memo:
                return memo[n]
            
            total = 0
            for num in nums:
                if n - num >= 0:
                    total += ways(n - num, memo)
            
            memo[n] = total
            return memo[n]
        
        return ways(target, {})
                    
            



        