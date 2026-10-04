class Solution:
    def integerBreak(self, n: int) -> int:
        def rec(num, memo):
            if num <= 1:
                return 1
            
            if num in memo:
                return memo[num]
            
            res = 0 if n == num else num
            for i in range(1, num):
                c1 = 0
                if num - i >= 0:
                    c1 = i * rec(num - i, memo)
                c2 = i
                res = max(res, c1, c2)
            memo[num] = res
            return memo[num]

        return rec(n, {})
            

            
