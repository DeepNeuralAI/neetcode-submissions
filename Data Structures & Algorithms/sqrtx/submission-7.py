class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x

        res = 0
        while l <= r:
            m = (l + r) // 2
            candidate = m * m

            if candidate == x:
                return m
            
            if candidate < x:
                res = m
                l = m + 1
            else:
                r = m - 1
        
        return res

        