class Solution:
    def integerBreak(self, n: int) -> int:
        def rec(num, memo):
            if num == 2:
                return 1
            
            if num in memo:
                return memo[num]

            res = 0
            for i in range(1, num):
                res = max(
                    res,
                    i * (num - i),
                    i * rec(num - i, memo)
                )
            
            memo[num] = res
            return res
        
        return rec(n, {})


            
