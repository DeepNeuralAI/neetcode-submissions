class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l = 0
        r = x

        while l < r:
            m = (l + r) // 2
            candidate = m * m

            if candidate == x:
                return m
            
            if candidate < x:
                l = m + 1
            else:
                r = m
        
        return l - 1
        