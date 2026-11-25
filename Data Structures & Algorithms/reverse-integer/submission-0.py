class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x = x // 10
            res = (10 * res) + digit
        
            if not (-2**31 <= res <= 2**31 - 1):
                return 0
        
        return sign * res