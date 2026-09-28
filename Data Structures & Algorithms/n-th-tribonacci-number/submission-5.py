class Solution:
    def tribonacci(self, n: int) -> int:
        # Bottom Up
        if n == 0:
            return 0

        if n == 1:
            return 1
            
        res = [0] * (n + 1)
        res[1] = 1
        res[2] = 1

        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2] + res[i - 3]
        
        return res[n]