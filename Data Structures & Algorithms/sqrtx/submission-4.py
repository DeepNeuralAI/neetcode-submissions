class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = r

        while l <= r:
            m = (l + r) // 2
            val = m * m 
            if val == x:
                return m
            
            if val < x:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
        